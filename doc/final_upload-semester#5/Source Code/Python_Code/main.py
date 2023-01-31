import cv2
import threading
import time

from Logger import Logger
from MqttSender import MqttSender
from HttpStreamer import HttpStreamer
import Recognizer

from flask import Response
from flask import Flask

last_frame = None

def get_last_frame():
    global last_frame

    while True:
        if (last_frame is not None):
            frame = Recognizer.getImage(last_frame[0], last_frame[1])
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.3)

def start_http_server():
    app = HttpStreamer(get_last_frame)
    app.run()

def start_recognizer():
    mqttSender.subscribe()
    global last_frame

    camera = cv2.VideoCapture(0)

    while(True):
        ret, image = camera.read()
        result = Recognizer.hogDetector(image.copy())
        last_frame = [result, image]
        mqttSender.send(len(result))

logger = Logger("Main")
logger.info("Start theObserver...")

mqttSender = MqttSender.loadConfigFromYamlFile('config.yaml')

logger.info("before creating thread")

thread_http_server = threading.Thread(target=start_http_server, daemon=True)
thread_recognizer = threading.Thread(target=start_recognizer, daemon=True)

logger.info("before running thread")
thread_http_server.start()
thread_recognizer.start()
logger.info("wait for the thread to finish")

while True:
    time.sleep(1)

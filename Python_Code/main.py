import cv2
import threading
import time

from Logger import Logger
from MqttSender import MqttSender
import Recognizer

from flask import Response
from flask import Flask

results = []

def start_http_server():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route("/video_feed")
    def video_feed():
        # return the response generated along with the specific media
        # type (mime type)
        return Response(gen_frames(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")

    def gen_frames():
        while True:
            if (len(results) > 0):
                frame = Recognizer.getImage(results[-1][0], results[-1][1])
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(1)

    app.run(debug=True, use_reloader=False)
    return
    while (True): 
        if (len(results) > 0):
            print(len(results[-1][1]))
        time.sleep(0.5)

def start_recognizer():
    camera = cv2.VideoCapture(0)

    while(True):
        ret, image = camera.read()
        result = Recognizer.hogDetector(image.copy())
        results.append([result, image])
        mqttSender.send(len(result))
        #result1 = len(result) # anzahl der besucher
        #print (result1)

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

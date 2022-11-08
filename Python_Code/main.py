import cv2
import threading
import time

from Logger import Logger
from MqttSender import MqttSender
from Recognizer import hogDetector

lastResult = 0

def start_http_server():
    lastlastResult = 0
    while (True): 
        if (lastlastResult != lastResult):
            print(lastResult)
            lastlastResult = lastResult

def start_recognizer():
    camera = cv2.VideoCapture(0)

    while(True):
        ret, image = camera.read()
        result = hogDetector(image.copy())
        lastResult = len(result)
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
thread_http_server.join()
thread_recognizer.join()
logger.info("all done")

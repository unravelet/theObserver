import cv2
import imutils
from imutils.object_detection import non_max_suppression
import numpy as np
import time
import base64
from PIL import Image
from matplotlib import pyplot as plt

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def hogDetector(image):
   #image = imutils.resize(image, width=min(400, image.shape[1]))
   clone = image.copy()
   rects, weights = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.1)
   for (x, y, w, h) in rects:
       cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
   rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
   result = non_max_suppression(rects, probs=None, overlapThresh=0.7)
   return result

def getImage(result, image):
    for (xA, yA, xB, yB) in result: 
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    return image

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)

    while(True):
        ret, image = camera.read()

        start_time = time.time()
        result = hogDetector(image.copy())
        print("--- %s seconds ---" % (time.time() - start_time))

        result1 = len(result) # anzahl der besucher
        print (result1)
        
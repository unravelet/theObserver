import cv2
import imutils
# from imutils.video import VideoStream
# from imutils.video import FPS
# from threading import Thread
# import time
# from datetime import datetime, time
# import numpy as np
# import mediapipe as mp
# import argparse
import yaml

from mqtt import Mqtt

#######################################################################################



with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    client = Mqtt(config["mqtt_broker"], config["mqtt_port"], config["mqtt_topic"])


##Initializing the HOG person detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

##
cap = cv2.VideoCapture('../res/videos/video2.mp4')
if not cap.isOpened():
  print("Error. Source file not found.")
else:
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("fps of current video file: ", fps)
##

while cap.isOpened():
    # Reading the video stream
    ret, image = cap.read()
    if ret:
        image = imutils.resize(image,
                               width=min(400, image.shape[1]))

        # Detecting all the regions
        # in the Image that has a
        # pedestrians inside it
        (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)

        # Drawing the regions in the
        # Image
        person = 1
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1

        # Send counter to mqtt broker
        client.send(str(person - 1))

        # Showing the output Image
        cv2.putText(image, f'person {person - 1}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
client.disconnect()


#######################################################################################
## Example code from: https://nrsyed.com/2018/07/05/multithreading-with-opencv-python-to-improve-video-processing-performance/
## Multithreading version (Windows does not need this version)


# class CountsPerSec:
#     """
#     Class that tracks the number of occurrences ("counts") of an
#     arbitrary event and returns the frequency in occurrences
#     (counts) per second. The caller must increment the count.
#     """
#
#     def __init__(self):
#         self._start_time = None
#         self._num_occurrences = 0
#
#     def start(self):
#         self._start_time = datetime.now()
#         return self
#
#     def increment(self):
#         self._num_occurrences += 1
#
#     def countsPerSec(self):
#         elapsed_time = (datetime.now() - self._start_time).total_seconds()
#         # To run on windows you need to catch division by 0 (Linux ignores by default).
#         if elapsed_time == 0:
#             return 0
#         else:
#             return self._num_occurrences / elapsed_time
#
# #######################################################################################
#
#
# def putIterationsPerSec(frame, iterations_per_sec):
#     """
#     Add iterations per second text to lower-left corner of a frame.
#     """
#
#     cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
#         (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
#     return frame
#
# #######################################################################################
#
#
# class VideoGet:
#     """
#     Class that continuously gets frames from a VideoCapture object
#     with a dedicated thread.
#     """
#
#     def __init__(self, src=''):
#         self.stream = cv2.VideoCapture(src)
#         if not self.stream.isOpened():
#             print("Error. File not found.")
#             quit()
#         else:
#             fps = int(self.stream.get(cv2.CAP_PROP_FPS))
#             print("FPS: ", fps)
#             (self.grabbed, self.frame) = self.stream.read()
#             self.stopped = False
#
#     def start(self):
#         Thread(target=self.get, args=()).start()
#         return self
#
#     def get(self):
#         while not self.stopped:
#             if not self.grabbed:
#                 self.stop()
#             else:
#                 (self.grabbed, self.frame) = self.stream.read()
#
#     def stop(self):
#         self.stopped = True
#
# #######################################################################################
#
#
# class VideoShow:
#     """
#     Class that continuously shows a frame using a dedicated thread.
#     """
#
#     def __init__(self, frame=None):
#         self.frame = frame
#         self.stopped = False
#
#     def start(self):
#         Thread(target=self.show, args=()).start()
#         return self
#
#     def show(self):
#         hog = cv2.HOGDescriptor()
#         hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#         while not self.stopped:
#             self.frame = imutils.resize(self.frame, width=min(400, self.frame.shape[1]))
#            # Detecting all the regions
#            # in the Image that has a
#            # pedestrians inside it
#             (regions, _) = hog.detectMultiScale(self.frame,
#                                                winStride=(4, 4),
#                                                padding=(4, 4),
#                                                scale=1.05)
#            # Drawing the regions in the
#            # Image
#             for (x, y, w, h) in regions:
#                cv2.rectangle(self.frame, (x, y),
#                              (x + w, y + h),
#                              (0, 0, 255), 2)
#
#             cv2.imshow("Video", self.frame)
#             if cv2.waitKey(1) == ord("q"):
#                 self.stopped = True
#
#     def stop(self):
#         self.stopped = True
#
# #######################################################################################
#
#
# def threadBoth(source=''):
#     """
#     Dedicated thread for grabbing video frames with VideoGet object.
#     Dedicated thread for showing video frames with VideoShow object.
#     Main thread serves only to pass frames between VideoGet and
#     VideoShow objects/threads.
#     """
#
#     video_getter = VideoGet(source).start()
#     video_shower = VideoShow(video_getter.frame).start()
#     cps = CountsPerSec().start()
#
#     while True:
#         if video_getter.stopped or video_shower.stopped:
#             video_shower.stop()
#             video_getter.stop()
#             break
#
#         frame = video_getter.frame
#         frame = putIterationsPerSec(frame, cps.countsPerSec())
#         video_shower.frame = frame
#         cps.increment()
#
#
# threadBoth('../res/videos/video2.mp4')



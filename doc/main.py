import cv2
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import time
#from datetime import datetime, time
import numpy as np
#import mediapipe as mp




# cap = cv2.VideoCapture(1)
#
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break




#######################################################################################
# first try of recognizing people from video

def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('theObserver_demo_data', frame)
    return frame


def humanDetector():
    video_path = "../videos/video2.mp4"

    #writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (800, 600))
    writer = None
    if video_path is not None:
        print('[INFO] Opening Video from path.')
        detectByPathVideo(video_path, writer)
    else:
        print("ERROR: File not Found")
        return False


def detectByPathVideo(path, writer):
    video = cv2.VideoCapture(path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    print("fps of current video file: ", fps)
    check, frame = video.read()
    if not check:
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return
    print('Detecting people...')
    while True:
        # check is True if reading was successful
        check, frame = video.read()
        #frame = imutils.resize(frame, width=min(800, frame.shape[1]))
        frame = detect(frame)

        if writer is not None:
            writer.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or not check:
            video.release()
            cv2.destroyAllWindows()
            break


HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  #pre-trained model human detection

humanDetector()


#######################################################################################
## open and run video from given path

# video = cv2.VideoCapture("../videos/video1.mp4")
# fps = int(video.get(cv2.CAP_PROP_FPS))
# print("fps of current video file: ", fps)
#
# if not video.isOpened():
#     print("ERROR: File not found.")
#
# ret, frame = video.read()
# while True:
#     #check if frames are returning
#     ret, frame = video.read()
#
#     #opencv automatically speeds up video, needs to slow down to original pace
#     time.sleep(0.5/fps)
#
#     #displaying the frames of video
#     cv2.imshow('theObserver_demo_data', frame)
#
#     #quit video before end with command 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
#         video.release()
#         cv2.destroyAllWindows()
#         break

#######################################################################################
## try of recognizing people pose (computervision.zone)


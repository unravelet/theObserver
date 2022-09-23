import concurrent.futures
import multiprocessing
from multiprocessing.context import Process
import cv2
import imutils
import numpy as np
import time
import os


# Worker processes
def getframepipe(pipe_in):
    stopped = False
    cap = cv2.VideoCapture('./resource/daheim.mp4')
    if not cap.isOpened():
        cap.release()
        print("Error: Source not found.")

    while not stopped:
        ret, image = cap.read()
        if not ret:
            print(ret)
            print("frames finished")
            pipe_in.send(None)
            stopped = True
            cap.release()
            continue
        else:
            image = imutils.resize(image, width=min(400, image.shape[1]))
            #cv2.imshow("image", image)
            #if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
                #print("stopping loop")
                #frames.put(None)
                #break
            pipe_in.send(image)


def detectpersonPipe(pipe_out, pipe_in):
    # Setup ppl descriptor
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    altframe = pipe_out.recv()

    while altframe is not None:
        (regions, _) = hog.detectMultiScale(altframe, winStride=(4, 4), padding=(4, 4), scale=1.05)

        for (x, y, w, h) in regions:
            cv2.rectangle(altframe, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(altframe, f'person', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        #print(f'{os.getpid()} putting frame in queue')
        pipe_in.send(altframe)
        altframe = pipe_out.recv()

    pipe_out.send(None)
    print("altframe finished")


def getframe(frames):
    stopped = False
    cap = cv2.VideoCapture('./resource/demo1.mp4')
    if not cap.isOpened():
        cap.release()
        print("Error: Source not found.")

    while not stopped:
        ret, image = cap.read()
        if not ret:
            print(ret)
            print("frames finished")
            frames.put(None)
            stopped = True
            cap.release()
            continue
        else:
            print(f"{os.getpid()}: puttin frame into queue")
            image = imutils.resize(image, width=min(400, image.shape[1]))
            #cv2.imshow("image", image)
            #if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
                #print("stopping loop")
                #frames.put(None)
                #break
            frames.put(image)


def detectperson(frames, altframes):
    # Setup ppl descriptor
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    altframe = frames.get()

    while altframe is not None:
        (regions, _) = hog.detectMultiScale(altframe, winStride=(4, 4), padding=(4, 4), scale=1.05)

        for (x, y, w, h) in regions:
            cv2.rectangle(altframe, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(altframe, f'person', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        print(f'{os.getpid()}: putting frame in queue')
        altframes.put(altframe)
        altframe = frames.get()

    altframes.put(None)
    print("altframe finished")


def showImage():
    print("showing image")

def main():
    print("setup for process and queues")
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    frames = multiprocessing.Queue()
    altframes = multiprocessing.Queue()

    frames_in, frames_out = multiprocessing.Pipe()
    final_in, final_out = multiprocessing.Pipe()

    capture1 = multiprocessing.Process(target=getframe, args=(frames,))
    draw1 = multiprocessing.Process(target=detectperson, args=(frames, altframes))
    #draw2 = multiprocessing.Process(target=detectperson, args=(frames, altframes))
    #draw3 = multiprocessing.Process(target=detectperson, args=(frames, altframes))
    #draw4 = multiprocessing.Process(target=detectperson, args=(frames, altframes))

    #Example using pipes
    # capture1 = multiprocessing.Process(target=getframepipe, args=(frames_in,))
    # draw1 = multiprocessing.Process(target=detectpersonPipe, args=(frames_out, final_in))





    capture1.start()
    draw1.start()
    #draw2.start()
    #draw3.start()
    #draw4.start()

    # img = final_out.recv()
    # while img is not None:
    #     print("reading final image")
    #     cv2.imshow("final", img)
    #     img = final_out.recv()

    img = altframes.get()
    while img is not None:
        print(f"{os.getpid()}: showing final frame")
        cv2.imshow("final", img)
        cv2.waitKey(1)
        img = altframes.get()

    cv2.destroyAllWindows()
    capture1.join()
    draw1.join()
    #draw2.join()
    #draw3.join()
    print("Shutdown...")


if __name__ == "__main__":
    main()


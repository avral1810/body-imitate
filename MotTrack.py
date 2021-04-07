from imutils.video.FileVideoStream import *
import numpy as np
import cv2
import argparse
import time
import mediapipe as mp
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to video file")

args = vars(ap.parse_args())

fvs = FileVideoStream(args["video"], multithread=False).start()
fps = FPS()
time.sleep(1)

while fvs.more():
    frame = fvs.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    newFPS = fps.fps()
    cv2.putText(frame, f"FPS: {newFPS[1]}", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()


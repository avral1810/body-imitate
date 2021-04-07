import cv2
import mediapipe as mp
import time



mpPose, mpDraw = mp.solutions.pose, mp.solutions.drawing_utils
pose = mpPose.Pose()
cap = cv2.VideoCapture('./test.m4v')

ptime = ctime = newFPS = count = 0
refreshRate = 10


while 1:
    _, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    ctime = time.time()
    newFPS += 1 / (ctime - ptime)
    ptime = ctime
    if count % refreshRate == 0:
        fps = newFPS / refreshRate
        count += 1
        newFPS = 0
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 255), 3)
    count += 1
    cv2.imshow('VideoStream', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

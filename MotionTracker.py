import cv2
import mediapipe as mp
class MotionTracker:
    mpPose, mpDraw = mp.solutions.pose, mp.solutions.drawing_utils
    def __init__(self):
        self.pose = self.mpPose.Pose()


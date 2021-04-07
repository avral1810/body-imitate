import cv2
import time
from threading import Thread
from queue import Queue

class FileVideoStream:
    def __init__(self, source = 0, queueSize = 128, multithread=True):
        self.stream = cv2.VideoCapture(source)
        self.stopped = False
        self.Q = Queue(maxsize=queueSize)
        self.multithread = multithread
        print("Video Stream Inititated")

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while 1:
            if self.stopped:
                return
            if not self.Q.full():
                (grabbed, frame) = self.stream.read()
                if not grabbed:
                    self.stop()
                    return
                self.Q.put(frame)

    def read(self):
        return self.Q.get()

    def more(self):
        return self.Q.qsize() > 0

    def stop(self):
        self.stopped = True

class FPS:
    def __init__(self, refreshrate = 10):
        self.currTime = time.time()
        self.prevTime = 0
        self.count = 0
        self.add = 0
        self.refreshrate = refreshrate
        self._fps = 0

    def fps(self):
        self.add += 1/(self.currTime - self.prevTime)
        self.count += 1
        if self.count == self.refreshrate:
            self._fps = self.add//self.refreshrate
            self.count = 0
            self.add = 0
            return True, self._fps
        self.prevTime = self.currTime
        self.currTime = time.time()
        return False, self._fps


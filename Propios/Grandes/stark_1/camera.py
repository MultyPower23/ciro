import cv2

class Camera:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cam.read()
        return frame
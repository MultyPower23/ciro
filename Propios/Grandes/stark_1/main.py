from camera import Camera
from hand_tracker import HandTracker
from particle_system import ParticleSystem
import cv2

cam = Camera()
tracker = HandTracker()
particles = ParticleSystem()

while True:

    frame = cam.get_frame()

    hand_data = tracker.process(frame)

    if hand_data:
        x, y = hand_data
        particles.emit(x, y)

    particles.update(frame)

    cv2.imshow("Holo Hands", frame)

    if cv2.waitKey(1) == 27:
        break
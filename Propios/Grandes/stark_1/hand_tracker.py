import mediapipe as mp
import cv2

class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

        self.mp_draw = mp.solutions.drawing_utils

    def process(self, frame):

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(frameRGB)

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

                index = hand.landmark[8]

                h, w, _ = frame.shape

                x = int(index.x * w)
                y = int(index.y * h)

                return x, y

        return None
import mediapipe as mp
import numpy as np
# import cv2

mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands

def render_landmarks(image, hand_landmarks):
    mp_drawing.draw_landmarks(
            image, 
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        #     mp_drawing_styles. DrawingSpec(color=(36, 182, 255), thickness=1, circle_radius=2),
        #     mp_drawing_styles.DrawingSpec(color=(10,226,130), thickness=1, circle_radius=2)
            )
    # return mp_drawing
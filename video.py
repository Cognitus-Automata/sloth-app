import mediapipe as mp
import numpy as np
import cv2
# from func.HandTracking import HandDetector
# from func.track_hands import render_landmarks
# from track_hands import render_landmarks

mp_drawing_styles = mp.solutions.drawing_styles
from functions.track_hands import render_landmarks
# from utils.HandTracking import HandDetector

mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands


def open_cam(video_device = 0):

    cap = cv2.VideoCapture(video_device)

    # Instance Mediapipe
    # Hand accessing Hand estimation model
    # hand = HandDetector()

    with mp_hands.Hands(
                        static_image_mode=True,
                        max_num_hands=2,
                        min_detection_confidence=0.5) as hands:

        while True:
            ret, image = cap.read()
            if not ret:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                break
            else:
                # Detect & render
            
                # Recolor to RGB
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


                results = hands.process(image)
                # lmList = hands.findPosition(img, draw=False)
                    # Draw the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        render_landmarks(image, hand_landmarks)

                        # mp_drawing.draw_landmarks(
                        #     image,
                        #     hand_landmarks,
                        #     mp_hands.HAND_CONNECTIONS,
                        #     mp_drawing_styles.get_default_hand_landmarks_style(),
                        #     mp_drawing_styles.get_default_hand_connections_style())

            
                ret, buffer = cv2.imencode('.jpg', image)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




# open_cam(0)
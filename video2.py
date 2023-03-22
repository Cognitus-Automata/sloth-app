import mediapipe as mp
import numpy as np
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


from func.HandTracking import HandDetector
from func.track_hands import render_landmarks
# from track_hands import render_landmarks

# from utils.track_hands import render_landmarks
# from utils.HandTracking import HandDetector

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# hands = mp_hands.Hands()
mp_hands = mp.solutions.hands

def open_camera(video_device = 0):
    cap = cv2.VideoCapture(video_device)

    # Instance Mediapipe
    # Pose accessing Pose estimation model
    with mp_pose.Pose(min_detection_confidence = 0.5,
                    min_tracking_confidence = 0.5) as pose:
        
        while cap.isOpened():
            ret, frame = cap. read()
            if not ret:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # Detect & render
            
            # Recolor to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Make detection
            results = pose.process(image)
            # results = pose.process(image)
            
            # Recolor to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



            # Extrack Landmarks
            try:
                landmarks = results.pose_landmarks.landmark
            except:
                pass

            # Render detections
            render_landmarks(image, results)
        






            cv2.imshow('Mediapipe feed', image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

# open_camera(0)


    
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands()

def open_cam2(video_device = 0):

    cap = cv2.VideoCapture(video_device)

    # Instance Mediapipe
    # Hand accessing Hand estimation model
    # hand = HandDetector()

    with mp_hands.Hands(static_image_mode=True,
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
                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

            
            # cv2.imshow('Mediapipe feed', frame)
                ret, buffer = cv2.imencode('.jpg', image)
                # if ret:
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                # yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')
        # if cv2.waitKey(10) & 0xFF == ord('q'):
        #     break
        # else:
        #     cap.release()
        #     cv2.destroyAllWindows()



open_cam2(0)
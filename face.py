import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# Load hand detection model
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip and convert to RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmarks for gesture recognition
                landmarks = np.array([[lm.x, lm.y] for lm in hand_landmarks.landmark])

                # Define gesture conditions
                thumb_tip = landmarks[4]
                index_tip = landmarks[8]
                middle_tip = landmarks[12]
                ring_tip = landmarks[16]
                pinky_tip = landmarks[20]

                if thumb_tip[1] < index_tip[1] and thumb_tip[1] < middle_tip[1]:
                    gesture = "Thumbs Up 👍"
                elif thumb_tip[1] > index_tip[1] and thumb_tip[1] > middle_tip[1]:
                    gesture = "Thumbs Down 👎"
                elif index_tip[1] < middle_tip[1] < ring_tip[1] < pinky_tip[1]:
                    gesture = "Victory ✌️"
                else:
                    gesture = "Unknown Gesture"

                # Display gesture on screen
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the webcam feed
        cv2.imshow("Hand Gesture Recognition", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()

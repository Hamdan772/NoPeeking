import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

# Eye landmark indices (iris and surrounding landmarks)
LEFT_EYE_LANDMARKS = [33, 133]  # Outer corners
RIGHT_EYE_LANDMARKS = [362, 263]

class GazeDetector:
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def is_looking_away(self, frame):
        # Convert to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return False  # No face found = assume OK

        for face_landmarks in results.multi_face_landmarks:
            left_eye = face_landmarks.landmark[LEFT_EYE_LANDMARKS[0]]
            right_eye = face_landmarks.landmark[RIGHT_EYE_LANDMARKS[1]]

            # Calculate relative eye positions
            dx = abs(left_eye.x - right_eye.x)
            dy = abs(left_eye.y - right_eye.y)

            # Heuristic: if eyes are too vertical (face turned), user is not looking at screen
            if dy / dx > 0.15:
                return True  # User is looking away

        return False

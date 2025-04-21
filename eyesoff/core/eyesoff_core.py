import cv2
import time
import mediapipe as mp
from core.utils import save_snapshot, play_alert_sound, log_event

# Initialize MediaPipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Define indices for left and right irises
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

def get_iris_center(landmarks, indices):
    x = int(sum([landmarks[i].x for i in indices]) / len(indices) * 640)
    y = int(sum([landmarks[i].y for i in indices]) / len(indices) * 480)
    return x, y

def is_looking_away(left_iris, right_iris):
    # Simple logic: if iris x-coordinates are far from center
    lx, _ = left_iris
    rx, _ = right_iris
    center_x = 640 // 2
    return lx < center_x - 80 or lx > center_x + 80 or rx < center_x - 80 or rx > center_x + 80

def run_eyesoff():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    print("[🎥] Webcam initialized at 640x480")
    print("[🔒] EyesOff is running. Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                left_iris = get_iris_center(face_landmarks.landmark, LEFT_IRIS)
                right_iris = get_iris_center(face_landmarks.landmark, RIGHT_IRIS)

                if is_looking_away(left_iris, right_iris):
                    log_event("👀 User looking away from screen.")
                    save_snapshot(frame)
                    try:
                        play_alert_sound()
                    except Exception as e:
                        print(f"[⚠️] Failed to play sound: {e}")
        else:
            log_event("No face detected.")

        # Exit on Q key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[👋] EyesOff exited cleanly.")

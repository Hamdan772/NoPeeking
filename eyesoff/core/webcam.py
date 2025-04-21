import cv2

def get_camera(width=640, height=480, cam_index=0):
    cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)  # CAP_DSHOW for Windows compatibility

    if not cap.isOpened():
        raise RuntimeError("❌ Could not open webcam.")

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    print(f"[🎥] Webcam initialized at {width}x{height}")
    return cap

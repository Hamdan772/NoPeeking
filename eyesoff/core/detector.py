import cv2
import os

# Path to the YuNet model (you’ll need to download this once)
MODEL_PATH = r"C:\Users\epoka\OneDrive\Pictures\face_detection_yunet_2023mar.onnx"

class YuNetDetector:
    def __init__(self, input_width=320, input_height=320, conf_threshold=0.9):
        self.input_size = (input_width, input_height)
        self.conf_threshold = conf_threshold

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"YuNet model not found at: {MODEL_PATH}")

        self.detector = cv2.FaceDetectorYN.create(
            model=MODEL_PATH,
            config="",
            input_size=self.input_size
        )

    def set_input_size(self, width, height):
        self.detector.setInputSize((width, height))

    def detect_faces(self, frame):
        h, w = frame.shape[:2]
        if (w, h) != self.input_size:
            self.set_input_size(w, h)

        # Detect faces
        _, faces = self.detector.detect(frame)

        results = []
        if faces is not None:
            for face in faces:
                x, y, w, h, conf = face[:5]
                if conf >= self.conf_threshold:
                    results.append({
                        "box": (int(x), int(y), int(w), int(h)),
                        "confidence": float(conf)
                    })
        return results

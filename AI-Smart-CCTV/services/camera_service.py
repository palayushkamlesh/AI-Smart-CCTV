import cv2
import os
from datetime import datetime

from ai.face_service import recognize_faces
from services.security_service import handle_unknown
from utils.video_recorder import write_frame

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("❌ Error: Could not open webcam")

os.makedirs("screenshots", exist_ok=True)

faces = []
frame_count = 0


def get_camera():
    return camera


def generate_frames():

    global faces
    global frame_count

    while True:

        success, frame = camera.read()

        if not success:
            continue

        # Face recognition every 5th frame
        frame_count += 1

        if frame_count % 5 == 0:
            faces = recognize_faces(frame)

        # Draw detections
        for face in faces:

            color = (0, 255, 0)

            if face["name"] == "Unknown":
                color = (0, 0, 255)
                handle_unknown(frame)

            cv2.rectangle(
                frame,
                (face["left"], face["top"]),
                (face["right"], face["bottom"]),
                color,
                2
            )

            cv2.putText(
                frame,
                face["name"],
                (face["left"], face["top"] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

        # Write frame if recording
        write_frame(frame)

        ret, buffer = cv2.imencode(".jpg", frame)

        if not ret:
            continue

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + buffer.tobytes() +
            b'\r\n'
        )


def capture_image():

    success, frame = camera.read()

    if not success:
        return None

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"

    filepath = os.path.join("screenshots", filename)

    cv2.imwrite(filepath, frame)

    print("📸 Screenshot Saved:", filepath)

    return filepath
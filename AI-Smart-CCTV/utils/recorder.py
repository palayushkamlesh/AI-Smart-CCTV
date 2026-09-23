import cv2
import time
import os
from datetime import datetime

os.makedirs("recordings", exist_ok=True)


def record_video(camera, duration=15):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"

    filepath = os.path.join("recordings", filename)

    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(filepath, fourcc, 20, (width, height))

    start = time.time()

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        out.write(frame)

        cv2.imshow("Recording...", frame)

        if time.time() - start >= duration:
            break

        if cv2.waitKey(1) == ord("q"):
            break

    out.release()

    return filepath
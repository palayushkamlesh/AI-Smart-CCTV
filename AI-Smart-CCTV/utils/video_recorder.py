import cv2
import os
from datetime import datetime

os.makedirs("recordings", exist_ok=True)

video_writer = None
recording = False
current_video_path = None


def start_recording(camera):

    global video_writer
    global recording
    global current_video_path

    if recording:
        return

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".mp4"

    current_video_path = os.path.join(
        "recordings",
        filename
    )

    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = camera.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 20

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    video_writer = cv2.VideoWriter(
        current_video_path,
        fourcc,
        fps,
        (width, height)
    )

    if not video_writer.isOpened():
        print("❌ Failed to create video writer")
        return

    recording = True

    print("🎥 Recording Started")
    print(current_video_path)


def write_frame(frame):

    global recording
    global video_writer

    if recording and video_writer is not None:
        video_writer.write(frame)


def stop_recording():

    global recording
    global video_writer

    if not recording:
        return

    recording = False

    if video_writer is not None:
        video_writer.release()
        video_writer = None

    print("⏹ Recording Saved")


def is_recording():
    return recording
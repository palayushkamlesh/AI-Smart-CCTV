from utils.video_recorder import (
    start_recording,
    stop_recording
)

recording = False


def start(camera):

    global recording

    if recording:
        print("⚠️ Recording already running")
        return

    start_recording(camera)

    recording = True

    print("🎥 Recording Started")


def stop():

    global recording

    if not recording:
        print("⚠️ Recording is not running")
        return

    stop_recording()

    recording = False

    print("⏹ Recording Stopped")
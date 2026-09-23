from flask import Blueprint, render_template, Response, redirect, url_for

from services.camera_service import (
    generate_frames,
    capture_image,
    get_camera
)

from services.recording_service import (
    start,
    stop
)

dashboard = Blueprint("dashboard", __name__)

camera = get_camera()


@dashboard.route("/")
def home():
    return render_template("dashboard.html")


@dashboard.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@dashboard.route("/capture")
def capture():

    capture_image()

    return redirect(url_for("dashboard.home"))


@dashboard.route("/start_recording")
def start_recording():

    start(camera)

    return redirect(url_for("dashboard.home"))


@dashboard.route("/stop_recording")
def stop_recording():

    stop()

    return redirect(url_for("dashboard.home"))
from flask import Blueprint, render_template, redirect, url_for

from services.camera_service import get_camera
from services.recording_service import start, stop
from services.alarm_service import start_alarm

remote = Blueprint("remote", __name__)

camera = get_camera()


@remote.route("/remote")
def home():
    return render_template("remote.html")


@remote.route("/remote/capture")
def capture():

    from services.camera_service import capture_image

    capture_image()

    return redirect(url_for("remote.home"))


@remote.route("/remote/start")
def start_recording():

    start(camera)

    return redirect(url_for("remote.home"))


@remote.route("/remote/stop")
def stop_recording():

    stop()

    return redirect(url_for("remote.home"))


@remote.route("/remote/alarm")
def alarm():

    start_alarm()

    return redirect(url_for("remote.home"))
import cv2
import face_recognition
import pickle
import time

from ai.evidence import save_screenshot
from utils.hash import generate_sha256
from email_service.gmail_sender import send_email
from database.models import db, Detection
from flask import Flask
import config

# -------------------------
# Flask Database Setup
# -------------------------

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

# -------------------------
# Load Face Encodings
# -------------------------

with open("encodings/face_encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

cap = cv2.VideoCapture(0)

last_unknown_time = 0
cooldown = 15  # seconds

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(
            known_encodings,
            face_encoding,
            tolerance=0.5,
        )

        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2,
        )

        # -------------------------
        # Unknown Detection
        # -------------------------

                # -------------------------
        # Unknown Detection
        # -------------------------

        if name == "Unknown":

            current_time = time.time()

            if current_time - last_unknown_time > cooldown:

                image_path = save_screenshot(frame)

                sha256 = generate_sha256(image_path)

                try:
                    send_email(image_path)
                    print("Email Alert Sent")
                except Exception as e:
                    print("Email Error:", e)

                with app.app_context():

                    detection = Detection(
                        person_name="Unknown",
                        status="Unknown",
                        image_path=image_path,
                        video_path="",
                        sha256=sha256,
                    )

                    db.session.add(detection)
                    db.session.commit()

                print("Unknown person detected.")
                print("Screenshot:", image_path)

                last_unknown_time = current_time
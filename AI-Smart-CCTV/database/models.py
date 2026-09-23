from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Detection(db.Model):
    __tablename__ = "detections"

    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(100))
    status = db.Column(db.String(20))
    image_path = db.Column(db.String(255))
    video_path = db.Column(db.String(255))
    sha256 = db.Column(db.String(255))
    camera_id = db.Column(db.String(50), default="CAM-001")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class SystemLog(db.Model):
    __tablename__ = "system_logs"

    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
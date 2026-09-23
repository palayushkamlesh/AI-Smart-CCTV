import cv2
import pickle
import face_recognition

# ---------------------------------
# Load Face Encodings
# ---------------------------------
with open("encodings/face_encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]


def recognize_faces(frame):

    # Resize frame for faster processing
    small_frame = cv2.resize(
        frame,
        (0, 0),
        fx=0.25,
        fy=0.25
    )

    # Convert BGR to RGB
    rgb = cv2.cvtColor(
        small_frame,
        cv2.COLOR_BGR2RGB
    )

    # Detect faces
    face_locations = face_recognition.face_locations(rgb)

    face_encodings = face_recognition.face_encodings(
        rgb,
        face_locations
    )

    results = []

    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            known_encodings,
            face_encoding,
            tolerance=0.5
        )

        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        # Scale coordinates back to original frame size
        results.append({
            "name": name,
            "top": top * 4,
            "right": right * 4,
            "bottom": bottom * 4,
            "left": left * 4
        })

    return results
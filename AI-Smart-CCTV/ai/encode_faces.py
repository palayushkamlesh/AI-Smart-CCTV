import face_recognition
import os
import pickle

KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "encodings/face_encodings.pkl"

known_encodings = []
known_names = []

for person_name in os.listdir(KNOWN_FACES_DIR):

    person_path = os.path.join(KNOWN_FACES_DIR, person_name)

    if not os.path.isdir(person_path):
        continue

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)

print("Total Faces Encoded:", len(known_encodings))

data = {
    "encodings": known_encodings,
    "names": known_names
}

os.makedirs("encodings", exist_ok=True)

with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump(data, f)

print("Face encodings saved successfully.")
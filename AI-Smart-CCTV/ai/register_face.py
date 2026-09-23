import cv2
import face_recognition
import os

person_name = input("Enter Person Name: ").strip()

save_path = f"known_faces/{person_name}"

os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

print("Press SPACE to capture image")
print("Press Q to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == ord(" "):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb)

        if len(faces) == 1:

            file_name = os.path.join(save_path, f"{count}.jpg")

            cv2.imwrite(file_name, frame)

            print(f"Saved {file_name}")

            count += 1

        else:

            print("Exactly one face must be visible.")

    elif key == ord("q"):

        break

cap.release()
cv2.destroyAllWindows()

print("Registration Complete")
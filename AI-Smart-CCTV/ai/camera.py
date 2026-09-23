import cv2
from datetime import datetime


class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise Exception("Unable to open webcam")

    def start(self):

        while True:

            ret, frame = self.cap.read()

            if not ret:
                break

            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            cv2.putText(
                frame,
                now,
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.imshow("AI Smart CCTV", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = Camera()
    camera.start()
import cv2
from utils.recorder import record_video

cap = cv2.VideoCapture(0)

print("Recording started...")

video = record_video(cap, 10)

cap.release()
cv2.destroyAllWindows()

print(video)
import cv2
import os
from datetime import datetime

os.makedirs("screenshots", exist_ok=True)

def save_screenshot(frame):

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"

    path = os.path.join("screenshots", filename)

    cv2.imwrite(path, frame)

    return path
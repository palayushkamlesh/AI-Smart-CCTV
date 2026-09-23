import time

from ai.evidence import save_screenshot
from utils.hash import generate_sha256
from email_service.gmail_sender import send_email
from services.alarm_service import start_alarm

last_unknown_time = 0
cooldown = 15


def handle_unknown(frame):

    global last_unknown_time

    current_time = time.time()

    if current_time - last_unknown_time < cooldown:
        return

    image_path = save_screenshot(frame)

    sha256 = generate_sha256(image_path)

    print("SHA256:", sha256)

    try:
        send_email(image_path)
        print("✅ Email Alert Sent")
        start_alarm()
    except Exception as e:
        print("❌ Email Error:", e)

    print("🚨 Unknown Person Detected")

    last_unknown_time = current_time
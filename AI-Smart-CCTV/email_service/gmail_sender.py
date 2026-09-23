import smtplib
from email.message import EmailMessage
import os

# Your Gmail
EMAIL_ADDRESS = "palayush0024@gmail.com"

# Gmail App Password
EMAIL_PASSWORD = "javr zwfb hurj ehod"

# Receiver
RECEIVER_EMAIL = "palayush0024@gmail.com"


def send_email(image_path):

    msg = EmailMessage()

    msg["Subject"] = "🚨 AI Smart CCTV Alert"

    msg["From"] = EMAIL_ADDRESS

    msg["To"] = RECEIVER_EMAIL

    msg.set_content(
        "Unknown person detected by AI Smart CCTV.\n\nScreenshot attached."
    )

    with open(image_path, "rb") as f:

        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="image",
        subtype="jpeg",
        filename=os.path.basename(image_path),
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)

    print("Email Sent Successfully")
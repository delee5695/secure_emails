import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Access the app password
app_pass = os.getenv('APP_PASS')  # Retrieve the API key
if not app_pass:
    raise EnvironmentError("APP_PASS not found in .env file or environment variables")


def send_email(message, receiver_email):

    subject = "An email!"
    message = message
    sender_email = "your_email"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email"
    smtp_password = app_pass

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        # print("Email notification sent successfully!")
    except Exception as e:
        print(f"Failed to send email notification: {e}")


send_email("hi", "recipient_email")
import smtplib
from email.mime.text import MIMEText
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
import os
import encryption

# Load variables from the .env file
load_dotenv()

# Access the app password
app_pass = os.getenv("APP_PASS")  # Retrieve the API key
my_email = os.getenv("MY_EMAIL")  # Retrieve sender email
receiver_email = os.getenv("RECEIVER_EMAIL") # Retrieve receiver email
if not app_pass:
    raise EnvironmentError("APP_PASS not found in .env file or environment variables")
if not my_email:
    raise EnvironmentError("MY_EMAIL not found in .env file or environment variables")
if not receiver_email:
    raise EnvironmentError("RECEIVER_EMAIL not found in .env file or environment variables")


def send_email(message, receiver_email):

    subject = "An email!"
    message = message
    sender_email = my_email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = my_email
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


# Load the recipient's public key from a PEM file
with open("recipient_public_key.pem", "rb") as pem_file:
    public_key = serialization.load_pem_public_key(pem_file.read())

# Encrypt the message
MESSAGE = "hello"
encrypted_message_hex = encryption.encrypt_message(MESSAGE, public_key)

send_email(encrypted_message_hex, receiver_email)

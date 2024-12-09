# For demo: Run this script to send an encrypted email message.

import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from ast import literal_eval
import os
import sys

# Import rsa module from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import rsa


# Load variables from the .env file
load_dotenv()

# Access the app password, sender email, and receiver email
app_pass = os.getenv("APP_PASS")  # Retrieve the API key
my_email = os.getenv("MY_EMAIL")  # Retrieve sender email
receiver_email = os.getenv("RECEIVER_EMAIL") # Retrieve receiver email
public_key = os.getenv("PUBLIC_KEY") # Retrieve public key
if not app_pass:
    raise EnvironmentError("APP_PASS not found in .env file or environment variables")
if not my_email:
    raise EnvironmentError("MY_EMAIL not found in .env file or environment variables")
if not receiver_email:
    raise EnvironmentError("RECEIVER_EMAIL not found in .env file or environment variables")
if not public_key:
    raise EnvironmentError("PUBLIC_KEY not found in .env file or environment variables")

# Convert the public key from a string to a tuple
public_key = literal_eval(public_key)


def convert_message_to_int(message):
    """
    Convert message (str) to a single long integer.
    
    Args:
        message: str containing your message

    Returns:
        message_as_int: the message converted to an integer (int)
    """
    # add a one at the beginning to prevent leading zeros from being cut off
    converted_message = "1"

    for i in message:
        int_letter = "{:04d}".format(
            ord(i)
        )  # Convert single letter to zero-padded ASCII
        converted_message += int_letter
    converted_message = int(converted_message)
    return converted_message  # Return as integer

def send_email(message, receiver_email):

    subject = "You got an encrypted message!"
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


# Enter a message to encrypt and send
MESSAGE = "Hello Sally!"

# Convert message to an integer
message_as_int = convert_message_to_int(MESSAGE)

# The message must be smaller than p*q to be encrypted correctly
if message_as_int >= public_key[0]:
    raise ValueError("The message in integer form must be smaller than p*q. Choose a shorter message or larger prime numbers.")

encrypted_message = rsa.encrypt(public_key, message_as_int)
encrypted_message = str(encrypted_message) # needs to be a string to send over email, but we'll convert it back to an int afterwards

# Send an email to your recipient containing the encrypted message
send_email(encrypted_message, receiver_email)
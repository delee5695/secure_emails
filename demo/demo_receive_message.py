# For demo: Run this script to read and decrypt the sent email message.

import imaplib
import email
from dotenv import load_dotenv
from ast import literal_eval
import os
import sys

# Import rsa module from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import rsa


# Access the app password
load_dotenv()
app_pass = os.getenv('APP_PASS')  # Retrieve the API key
my_email = os.getenv('MY_EMAIL')
private_key = os.getenv("PRIVATE_KEY") # Retrieve private key
if not app_pass:
    raise EnvironmentError("APP_PASS not found in .env file or environment variables")
if not my_email:
    raise EnvironmentError("MY_EMAIL not found in .env file or environment variables")
if not private_key:
    raise EnvironmentError("PRIVATE_KEY not found in .env file or environment variables")

# Convert the public key from a string to a tuple
private_key = literal_eval(private_key)


# Gmail IMAP settings
IMAP_SERVER = 'imap.gmail.com'
EMAIL = my_email
PASSWORD = app_pass

def read_emails():
    # Connect to Gmail
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)

    # Select the inbox
    mail.select("inbox")

    # Search for all emails
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()

    for e_id in email_ids[-1:]:  # Fetch the last 1 emails
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            message = part.get_payload(decode=True).decode()
                else:
                    message = msg.get_payload(decode=True).decode()

    mail.logout()

    return message

def convert_int_to_message(message_as_int):
    """
    Convert the long integer back to the original message.
    
    Args:
        message_as_int: int representing the encoded message

    Returns:
        message: the decoded string message
    """
    # Convert message_as_int into a string for processing
    message_as_int = str(message_as_int)[1:] # remove leading one
    
    # Increase the max string length for integer conversion
    original_message = ""
    for i in range(0, len(message_as_int), 4):
        original_message += chr(int(message_as_int[i : i + 4]))

    return original_message


# Retrieve the message from you email
if __name__ == "__main__":
    received_message = int(read_emails().split()[0])

# Decrypt the message
decrypted_message = rsa.decrypt(private_key, received_message)

# Convert back to letters
decrypted_message = convert_int_to_message(decrypted_message)

print("Decrypted message:", decrypted_message)
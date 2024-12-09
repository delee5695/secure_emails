import imaplib
import email
from dotenv import load_dotenv
import os

# Access the app password
load_dotenv()
app_pass = os.getenv('APP_PASS')  # Retrieve the API key
my_email = os.getenv('MY_EMAIL')
if not app_pass:
    raise EnvironmentError("APP_PASS not found in .env file or environment variables")
if not my_email:
    raise EnvironmentError("MY_EMAIL not found in .env file or environment variables")


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

if __name__ == "__main__":
    print(read_emails().split()[0])

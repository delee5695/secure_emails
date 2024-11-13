import imaplib
import email
from dotenv import load_dotenv
import os

# Access the app password
load_dotenv()
app_pass = os.getenv('APP_PASS')  # Retrieve the API key
if not app_pass:
    raise EnvironmentError("APP_PASS not found in .env file or environment variables")


# Gmail IMAP settings
IMAP_SERVER = 'imap.gmail.com'
EMAIL = 'your_email'
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

    for e_id in email_ids[-1:]:  # Fetch the last 5 emails
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                print("From:", msg["from"])
                print("Subject:", msg["subject"])
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            print(part.get_payload(decode=True).decode())
                else:
                    print(msg.get_payload(decode=True).decode())
                # print("-" * 50)

    mail.logout()

if __name__ == "__main__":
    read_emails()

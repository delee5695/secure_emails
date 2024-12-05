# secure_emails

How to run:

- Create a .env file with this format:
    APP_PASS="app password to your email account"
    MY_EMAIL="your email"
    RECEIVER_EMAIL="receiver's email"
- Have the person you're emailing run generate_keys.py to generate 
a public and private key and then send it to you (.pem file). Put that 
file in this folder.
- Run send_email to send an encrypted email to your recipient
- Have your recipient run check_email to get the email they received, 
decrypt it, and display the message
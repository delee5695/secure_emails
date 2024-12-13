from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import sys

# Increase max int digits
sys.set_int_max_str_digits(100000)


def convert_message_to_int(message):
    """convert message(str) to integers"""
    converted_message = ""
    for i in message:
        int_letter = "{:03d}".format(ord(i))  # convert single letter to integer
        converted_message += str(int_letter)
    return int(converted_message)


def encrypt_message(message, public_key):
    "get text message and encrypt it using public key"

    # Encrypt the message using the public key
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    # with open("encrypted_message.txt", "w") as file:
    #     file.write(encrypted_message.hex())
    return encrypted_message.hex()

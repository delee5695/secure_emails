from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def encrypt_message(message, public_key):
    "get text message and encrypt it using public key"

    # Encrypt the message using the public key
    encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    # with open("encrypted_message.txt", "w") as file:
    #     file.write(encrypted_message.hex())
    return encrypted_message.hex()

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load the recipient's public key from a PEM file
with open("public_key.pem", "rb") as pem_file:
    public_key = serialization.load_pem_public_key(pem_file.read())

# The message to be sent
message = b"Hello! This is a secure message."

# Encrypt the message using the public key
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

with open("encrypted_message.txt", "w") as file:
    file.write(encrypted_message.hex())

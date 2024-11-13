from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Read the encrypted message from the text file
with open("encrypted_message.txt", "r") as file:
    encrypted_message_hex = file.read().strip()  # Strip any whitespace or newline

# Convert the hexadecimal string back to bytes
encrypted_message = bytes.fromhex(encrypted_message_hex)

password = input("Enter your password: ")
# Load the private key from a PEM file
with open("private_key.pem", "rb") as pem_file:
    try:
        private_key = serialization.load_pem_private_key(
            pem_file.read(),
            password=password.encode(),  # Replace with the actual password
        )
    except ValueError:
        print("Wrong password")


# Decrypt the message
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("Decrypted message:", decrypted_message.decode())

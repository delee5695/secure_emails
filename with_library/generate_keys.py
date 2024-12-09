from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate a new RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)
password = input("Set up your password: ")

# Save the private key to a file in PEM format
with open("recipient_private_key.pem", "wb") as pem_file:
    pem_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(
                password.encode()
            ),  # Set your password
        )
    )

# Extract the public key from the private key
public_key = private_key.public_key()

# Save the public key to a PEM file
with open("recipient_public_key.pem", "wb") as pem_file:
    pem_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

# For demo: Run this script to generate a public and private key.

import sys
import os

# Import rsa module from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import rsa


# Choose two random prime numbers
p = 999999999999999999999999999999999841
q = 1001110111001011101010011000111110101

private_key, public_key = rsa.generate_key(p,q)

print("Add these to your .env file:")
print("Public key:", public_key)
print("Private key:", private_key)
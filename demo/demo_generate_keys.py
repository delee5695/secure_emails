# For demo: Run this script to generate a public and private key.

import sys
import os
from sympy import randprime

# Import rsa module from parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import rsa


# Generate two large prime numbers between 10^100 and 10^101
lower_bound = 10**100
upper_bound = 10**101

p = randprime(lower_bound, upper_bound)
print("First prime number:", p)
q = randprime(lower_bound, upper_bound)
while p == q: 
    q = randprime(lower_bound, upper_bound)
print("Second prime number:", q)


private_key, public_key = rsa.generate_key(p,q)

print("Add these to your .env file:")
print("Public key:", public_key)
print("Private key:", private_key)
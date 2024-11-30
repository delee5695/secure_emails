import rsa

# Enter two random prime numbers
p = 13
q = 29


# A message, converted to integer form
message = 103

# Check that the message is < p*q
if message >= p*q:
    raise ValueError("The message in integer form must be smaller than p*q")

private_key, public_key = rsa.generate_key(p,q)

encrypted_message = rsa.encrypt(public_key, message)
print("Encrypted message:", encrypted_message)

decrypted_message = rsa.decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)
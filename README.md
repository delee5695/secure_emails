# secure_emails

We created an implementation of RSA in python that doesn't use any external libraries. You can use our script to enter a message, encrypt it with RSA, send it to someone, and have them decrypt it.

### What's in this repo?

This repo contains three parts.

full_script.ipynb is a jupyter notebook that explains the process of RSA and walks you through running our RSA implementation code. This is the main component of our project.

with_library/ contains a more "official" implementation of RSA from pyca/cryptography. We used this as our initial draft to get a feel for how implementing RSA works.

demo/ contains scripts for running the in-class demo of our code.


### Sources
- https://www.teach.cs.toronto.edu/~csc110y/fall/notes/08-cryptography/05-rsa-cryptosystem-implementation.html
    - We used this sit as our intial source for explaining the math behind RSA, and we used the 
    encryption/decryption functions provided as a starting point for our RSA functions.
- pyca/cryptography: https://cryptography.io/en/latest/

# Modified from https://www.teach.cs.toronto.edu/~csc110y/fall/notes/08-cryptography/05-rsa-cryptosystem-implementation.html

import random
import math


def naive_modular_inverse(e, phi_n):
    """
    Return the modular inverse d of a number e, mod phi_n.

    Uses an easy to understand but inefficient method. Checks every
    possible value of d to see if multiplying it by e (mod phi_n)
    equals one.

    Not used.

    Args:
        e: number to be inverted (int)
        phi_n: the modulus (int)

    Returns:
        d: the modular inverse of e (int)
    """
    d = None

    for potential_d in range(0, phi_n - 1):
        x = e * potential_d % phi_n
    
        if x == 1:
            d = potential_d
            break

    if d is None:
        raise ValueError(f"No modular inverse exists for e={e} and phi_n={phi_n}.")
    
    return d


def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that
    gcd(a, b) == p * a + q * b.

    Helper function for modular_inverse.

    Returns:
        x: The gcd of a and b, your input numbers.
        p
        q

    Preconditions:
    - a >= 0
    - b >= 0

    >>> extended_euclidean_gcd(13, 10)
    (1, -3, 4)
    """
    x, y = a, b
    p_x, q_x = 1, 0  # Coefficients for x (initially 1 * a + 0 * b = a)
    p_y, q_y = 0, 1  # Coefficients for y (initially 0 * a + 1 * b = b)

    while y != 0:
        r = x % y
        quotient = x // y
        x, y = y, r

        # Update coefficients
        p_x, p_y = p_y, p_x - quotient * p_y
        q_x, q_y = q_y, q_x - quotient * q_y

    return x, p_x, q_x


def modular_inverse(e: int, phi_n: int) -> int:
    """Return the modular inverse d of e mod phi_n.

    Preconditions:
    - math.gcd(e, phi_n) == 1
    """
    gcd, p, q = extended_euclidean_gcd(e, phi_n)

    if gcd != 1:
        raise ValueError(f"No modular inverse exists for e={e} and phi_n={phi_n}")

    # Ensure the result is positive
    # p is the private key, and doing mod phi_n ensures it's within [0,phi_n-1]
    p = p % phi_n
    
    return p


def generate_key(p: int, q: int) -> \
        tuple[tuple[int, int], tuple[int, int]]:
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. The first tuple is the private key, containing (n, d).
      2. The second tuple is the public key, containing (n, e).

    Preconditions:
        - p and q are prime
        - p != q
    """
    # Compute the product of p and q
    n = p * q

    # Choose e such that gcd(e, phi_n) == 1.
    phi_n = (p - 1) * (q - 1)

    # Since e is chosen randomly, we repeat the random choice
    # until e is coprime to phi_n.
    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Choose d such that e * d % phi_n = 1.
    d = modular_inverse(e, phi_n)

    return ((n, d), (n, e))


def encrypt(public_key: tuple[int, int], plaintext: int) -> int:
    """ Encrypt the given plaintext using the recipient's public key.

    Preconditions:
        - public_key is a valid RSA public key (n, e)
        - 0 < plaintext < public_key[0]
    """
    n, e = public_key[0], public_key[1]


    # Directly computing plaintext ** e with large numbers is very 
    # computationally inefficient, but python has a built in 
    # function that implements it more efficiently.

    # This is the same as: encrypted = (plaintext ** e) % n
    encrypted = pow(plaintext, e, n)

    return encrypted


def decrypt(private_key: tuple[int, int], 
                message: int) -> int:
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (n, d)
        - 0 < ciphertext < private_key[0]
    """
    n, d = private_key[0], private_key[1]

    # This is the same as: decrypted = (message ** d) % n
    decrypted = pow(message, d, n)

    return decrypted
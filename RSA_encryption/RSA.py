#!/usr/bin/python
"""
Jack Weissenberger
CSC 222 Assignment 1: Digital Signatures
Using python 3.6.4
"""


def mod_exp(x, y, N):
    """
    This function performs modular exponentiation, taken from figure 1.4
    :param x: n-bit integer
    :param y: n-bit integer
    :param N: an integer exponent y
    :return: x^y mod N
    """

    y = int(y)
    x = int(x)
    N = int(N)
    #print(x,y,N)
    if y == 0:
        return 1

    z = mod_exp(x, (y//2), N)
    #print("z=", z)

    if (y % 2) == 0:
        return (z * z) % N
    else:
        return (x * z*z) % N


def exten_euclid(a, b):
    """
    Extended Eudlid's algorithm
    :param a: integer, a>=b>=0
    :param b: integer, a>=b>=0
    :return: integers x, y, d, such that d = gcd(a,b) and ax+by = d
    """

    if b == 0:
        return 1, 0, a

    x, y, d = exten_euclid(b, a % b)

    return y, x - (a//b)*y, d


def sign(message, N, e, p, q):
    """
    Takes a message and encodes it using RSA encryption
    :param message: the message you want to encrypt (this must be an integer)
    :param N: product of the two primes
    :param e: value that is relatively prime to (p-1)(q-1)
    :param p: the first prime
    :param q: the second prime
    :return: encoded: the encoded message, d: the private key
    """

    sudo = (p-1)*(q-1)
    # d is the secret key, the inverse of e mod (p-1)(q-1) computed with extended Euclid algorithm
    _, d, _, = exten_euclid(sudo, e)

    # keep adding sudo to d if it is still negative
    while d < 0:
        d = d + sudo

    # alice looks up the public key and sends y = (x^e mod N) computed using modular exponentiation (x is the message)
    # the message is then decoded by computing y^d mod N
    encoded = mod_exp(message, e, N)

    return encoded, d


def verify(orig_message, encoded_message, d, N):
    """
    Uses modular exponentiation to check if the encoded message matches the first message
    :param orig_message: the orig message before it was encoded
    :param encoded_message: the encoded message
    :param d: the private key
    :param N: the product of the two primes
    :return: Boolean True if the message was correctly encoded, or False if it was not
    """

    decoded_message = mod_exp(encoded_message, d, N)

    if decoded_message == orig_message:
        return True
    else:
        return False


if __name__ == "__main__":

    # pick two random primes p and q
    p = 101
    q = 761
    N = p*q
    # e is a 2n-bit number relatively prime to (p-1)(q-1)
    e = 3

    # must be a relatively small integer
    input_message = 32

    encoded, d = sign(input_message, N, e, p, q)

    result = verify(input_message, encoded, d, N)

    print("Was the message encoded correctly:", result)

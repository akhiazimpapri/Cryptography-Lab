import hashlib
import math
import random

# RSA Keys
def keys():
    p, q = 17, 23
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while math.gcd(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)
    return (d, n), (e, n)


# Hash Function
def hash_msg(msg):
    return hashlib.sha256(msg.encode()).hexdigest()


# RSA Encryption / Decryption
def rsa(key, x):
    e, n = key
    return pow(x, e, n)


# XOR Encryption / Decryption
def xor(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)


# Main 
private, public = keys()

message = input("Enter message: ")

# ---------------- Authentication ----------------

h = hash_msg(message)

# Digital Signature using private key
signature = [rsa(private, ord(c)) for c in h]


# ---------------- Confidentiality ----------------

# Random session key
session_key = random.randint(1, 100)

# Encrypt message
encrypted = xor(message, session_key)

# Encrypt session key using public key
encrypted_key = rsa(public, session_key)


# ---------------- Receiver ----------------

# Decrypt session key using private key
key = rsa(private, encrypted_key)

# Decrypt message
decrypted = xor(encrypted, key)


# Verify signature
received_hash = ''.join(
    chr(rsa(public, x)) for x in signature
)


# ---------------- Result ----------------

print("\nEncrypted Message:", encrypted)
print("Encrypted Session Key:", encrypted_key)
print("Decrypted Message:", decrypted)

if h == received_hash:
    print("Authentication: SUCCESS")
else:
    print("Authentication: FAILED")

if message == decrypted:
    print("Confidentiality: SUCCESS")
else:
    print("Confidentiality: FAILED")

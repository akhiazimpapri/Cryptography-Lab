import hashlib
import math
import random

# RSA KEY GENERATION
def generate_keys():

    p = 17
    q = 23

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while math.gcd(e, phi) != 1:
        e += 1
    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return private_key, public_key


# HASH FUNCTION
def hash_message(message):

    return hashlib.sha256(message.encode()).hexdigest()


# DIGITAL SIGNATURE
def create_signature(message, private_key):

    d, n = private_key

    h = hash_message(message)

    signature = []

    for ch in h:
        m = ord(ch)
        s = pow(m, d, n)
        signature.append(s)

    return signature


# VERIFY DIGITAL SIGNATURE
def verify_signature(message, signature, public_key):

    e, n = public_key

    h = hash_message(message)

    recovered_hash = ""

    for s in signature:

        m = pow(s, e, n)

        recovered_hash += chr(m)

    return h == recovered_hash


# SIMPLE SYMMETRIC ENCRYPTION
def encrypt(message, key):

    encrypted = []

    for ch in message:

        encrypted.append(ord(ch) ^ key)

    return encrypted


# SIMPLE SYMMETRIC DECRYPTION
def decrypt(ciphertext, key):

    message = ""

    for value in ciphertext:

        message += chr(value ^ key)

    return message


# MAIN PROGRAM
if __name__ == "__main__":

    # Generate RSA keys
    private_key, public_key = generate_keys()

    print("Public Key :", public_key)
    print("Private Key:", private_key)

    print("PGP SERVICES")

    print("1. Authentication")
    print("2. Confidentiality for transmitting data")
    print("3. Confidentiality for storing data")
    print("4. Authentication and Confidentiality")

    choice = int(input("\nEnter your choice: "))

    message = input("Enter your message: ")


    # 1. AUTHENTICATION

    if choice == 1:

        print("\n--- AUTHENTICATION ---")

        signature = create_signature(
            message,
            private_key
        )

        print("Digital Signature:", signature)

        result = verify_signature(
            message,
            signature,
            public_key
        )
        if result:
            print("Authentication: SUCCESS")
        else:
            print("Authentication: FAILED")


    # 2. CONFIDENTIALITY FOR TRANSMITTING DATA

    elif choice == 2:

        print("\n--- CONFIDENTIALITY FOR TRANSMITTING DATA ---")

        # Random session key
        session_key = random.randint(1, 100)

        print("Session Key:", session_key)

        # Encrypt message
        ciphertext = encrypt(
            message,
            session_key
        )

        print("Encrypted Data:", ciphertext)

        # ---------------- RECEIVER ----------------

        decrypted_message = decrypt(
            ciphertext,
            session_key
        )

        print("Decrypted Data:", decrypted_message)

        if message == decrypted_message:
            print("Confidentiality: SUCCESS")
        else:
            print("Confidentiality: FAILED")

    # 3. CONFIDENTIALITY FOR STORING DATA

    elif choice == 3:

        print("\n--- CONFIDENTIALITY FOR STORING DATA ---")

        # Generate session key
        session_key = random.randint(1, 100)

        # Encrypt message
        ciphertext = encrypt(
            message,
            session_key
        )

        # Store encrypted data
        with open("pgp_data.txt", "w") as file:

            file.write(str(session_key) + "\n")
            file.write(str(ciphertext))

        print("Encrypted data stored in pgp_data.txt")

        # Read stored data
        with open("pgp_data.txt", "r") as file:

            stored_key = int(file.readline())
            stored_ciphertext = eval(file.readline())

        # Decrypt stored data
        decrypted_message = decrypt(
            stored_ciphertext,
            stored_key
        )

        print("Decrypted Data:", decrypted_message)

        if message == decrypted_message:
            print("Storage Confidentiality: SUCCESS")
        else:
            print("Storage Confidentiality: FAILED")

    # 4. AUTHENTICATION + CONFIDENTIALITY

    elif choice == 4:

        print("\n--- AUTHENTICATION + CONFIDENTIALITY ---")

        # ---------------- AUTHENTICATION ----------------

        signature = create_signature(
            message,
            private_key
        )

        print("Digital Signature:", signature)

        # ---------------- CONFIDENTIALITY ----------------

        session_key = random.randint(1, 100)

        ciphertext = encrypt(
            message,
            session_key
        )

        print("Encrypted Data:", ciphertext)


        # ---------------- RECEIVER ----------------

        decrypted_message = decrypt(
            ciphertext,
            session_key
        )

        print("Decrypted Data:", decrypted_message)

        # Verify signature
        authenticated = verify_signature(
            decrypted_message,
            signature,
            public_key
        )
        if authenticated:
            print("Authentication: SUCCESS")
        else:
            print("Authentication: FAILED")

        if message == decrypted_message:
            print("Confidentiality: SUCCESS")
        else:
            print("Confidentiality: FAILED")
    else:
        print("Invalid choice!")
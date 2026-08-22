# Split the message into small blocks
def split_into_blocks(message, block_size):
    blocks = []

    for i in range(0, len(message), block_size):
        block = message[i:i + block_size]
        blocks.append(block)

    return blocks


# Encrypt each block using RSA
def rsa_encrypt(blocks, e, n):
    encrypted = []

    for block in blocks:
        cipher = pow(int(block), e, n)
        encrypted.append(cipher)

    return encrypted


# Decrypt each block using RSA
def rsa_decrypt(cipher_blocks, d, n):
    decrypted = []

    for cipher in cipher_blocks:
        plain = pow(cipher, d, n)
        decrypted.append(plain)

    return decrypted


# Convert blocks back into one string
def blocks_to_string(blocks, pad_size=None):
    result = ""

    for i in range(len(blocks)):
        block = str(blocks[i])

        # Add zeros before the block if necessary
        if pad_size and i < len(blocks) - 1:
            block = block.zfill(pad_size)

        result = result + block

    return result


if __name__ == "__main__":
    M = input("Enter the plaintext (numeric) M: ").strip()
    e = int(input("Enter public exponent e: "))
    d = int(input("Enter private exponent d: "))
    n = int(input("Enter modulus n: "))

    block_size = len(str(n)) - 1 

    # Encryption 
    plain_blocks = split_into_blocks(M, block_size)
    cipher_blocks = rsa_encrypt(plain_blocks, e, n)
    ciphertext = "".join(str(c) for c in cipher_blocks)

    # Decryption 
    decrypted_blocks = rsa_decrypt(cipher_blocks, d, n)
    decrypted_text = blocks_to_string(decrypted_blocks, pad_size=block_size)

    # Output 
    print("\n--- RESULTS ---")
    print(f"Plaintext (M)        : {M}")
    print(f"Block size used      : {block_size} digits")
    print(f"Plaintext blocks     : {plain_blocks}")
    print(f"Encrypted blocks     : {cipher_blocks}")
    print(f"Ciphertext (C)       : {ciphertext}")
    print(f"Decrypted blocks     : {decrypted_blocks}")
    print(f"Decrypted plaintext  : {decrypted_text}")
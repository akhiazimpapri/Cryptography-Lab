import hashlib

def sha_hash(text):
    # Create a SHA-256 hash object
    sha = hashlib.sha256()
    
    # Update the hash object with the bytes of the text
    sha.update(text.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return sha.hexdigest()

data = "Hello, World!"
print("Original Data:", data)
print("SHA-256 Hash:", sha_hash(data))
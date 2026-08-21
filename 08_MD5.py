import hashlib

def md5_hash(text):
    # Create an MD5 hash object
    md5 = hashlib.md5()
    
    # Update the hash object with the bytes of the text
    md5.update(text.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return md5.hexdigest()

data = "Hello, World!"
print("Original Data:", data)
print("MD5 Hash:", md5_hash(data))
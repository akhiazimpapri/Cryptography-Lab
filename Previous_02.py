# RSA Previous
def split_into_blocks(message, block_size):
  blocks = []

  for i in range(0, len(message), block_size):
    block = message[i : i + block_size]
    blocks.append(block)

  return blocks  

def rsa_encrypt(blocks, e, n):
  cipher = []
  for block in blocks:
    c = pow(int(block), e, n)
    cipher.append(c)

  return cipher

def rsa_decrypt(ciphers, d, n):
  plain = []
  for cipher in ciphers:
    m = pow(cipher, d, n)
    plain.append(m)

  return plain      

def block_to_string(blocks, pad_size):
  result = ""
  for i in range(len(blocks)):
    block = str(blocks[i])
    if pad_size and i < len(blocks)-1:
      block = block.zfill(pad_size)
    result += block
  return result      

text = "6882326879666683" 
e = 79
d = 1019
n = 3337 
block_plain = split_into_blocks(text, 3)
block_cipher = rsa_encrypt(block_plain, e, n)
cipher = block_to_string(block_cipher, pad_size=None)

decrypt_block = rsa_decrypt(block_cipher, d, n)
decrypted_msg = block_to_string(decrypt_block, None)
    
print("Original Message : ", text)    
print("Plain cipher : ", block_plain) 
print("Block cipher : ", block_cipher)   
print("Cipher Text ; ", cipher)
print("Decrypted Block : ", decrypt_block)
print("Decrypted Original Message : ", decrypted_msg)

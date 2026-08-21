import hashlib
import zlib
import math

def generate_key(p=23,q=17):
	n = p*q
	phi = (p-1)*(q-1)
	
	e = 2
	while math.gcd(e,phi)!=1:
		e+=1
	d = pow(e,-1,phi)
	private_key, public_key = (d,n),(e,n)
	return private_key, public_key
	
def hash1(message):
	encoded = message.encode()
	h = hashlib.sha256(encoded)
	return h.hexdigest()
	
def encryption(key, message):
	e, n = key
	ciphertext = []
	for char in (message):
		m = ord(char)
		c = pow(m,e,n)
		ciphertext.append(c)
	return ciphertext
def decryption(key, ciphertext):
	d,n = key
	message = ""
	for c in (ciphertext):
		m = pow(c,d,n)
		m = chr(m)
		message+=m
	return message

def sym_encryption(data,key):
	cipher = []
	for byte in data:
		cipher.append(byte^key)
	return bytes(cipher)

def sym_decryption(cipher, key):
	plain = []
	for byte in cipher:
		plain.append(byte^key)
	return bytes(plain)
	e
if __name__=="__main__":
	private_keyA, public_keyA = generate_key()
	private_keyB, public_keyB = generate_key()
	
	k = 123
	original_message = "The name of my country is Bangladesh"
	#sender
	h = hash1(original_message)
	ep = encryption(private_keyA, h)
	concatenated =   str(ep)+ "|" +original_message
	z = zlib.compress(concatenated.encode())
	
	ec = sym_encryption(z,k)
	ep = encryption(public_keyB,str(k))
	concatenated = str(ec)+"|"+str(ep)
	
	# reciever
	decrypted_compressed_msg, decrypted_pk = concatenated.split("|")
	decrypted_pk = eval(decrypted_pk)
	decrypted_compressed_msg = eval(decrypted_compressed_msg)
	
	dp = decryption(private_keyB, decrypted_pk)
	dc = sym_decryption(decrypted_compressed_msg, int(dp))
	
	m = zlib.decompress(dc)
	m = m.decode()
	
	encrypted_signature, msg = m.split("|")
	decrypted_signature = decryption(public_keyA, eval(encrypted_signature))
	hashed_msg = hash1(msg)
	
	#print(f"The original message is : {original_message}")
	print(f"Signature is {decrypted_signature}")
	print(f"Hash of msg is {hashed_msg}")
	if (decrypted_signature == hashed_msg):
		print("pgp successful")
	else:
		print ("Error")
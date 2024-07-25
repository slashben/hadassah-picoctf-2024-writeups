from Crypto.Cipher import DES
import binascii
import itertools

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def decrypt_with_key(key, msg):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(msg)

def encrypt_with_key(key, msg):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(msg)


known_plaintext = pad(binascii.unhexlify("10111213").decode())
known_ciphertext = binascii.unhexlify("0d559280a16f2706")
encrypted_flag = binascii.unhexlify("4d2520e2e1d24951df7c72fd99ad76888bc1b3d7f2084164066603cd14835470f9bde4a32f16427e")


encryption_dict = {}

possible_keys = [''.join(p).encode() for p in itertools.product('0123456789', repeat=6)]

for key1 in possible_keys:
    padded_key1 = pad(key1.decode())
    encrypted = encrypt_with_key(padded_key1, known_plaintext)
    encryption_dict[encrypted] = padded_key1

found_keys = None
for key2 in possible_keys:
    padded_key2 = pad(key2.decode())
    decrypted = decrypt_with_key(padded_key2, known_ciphertext)
    if decrypted in encryption_dict:
        key1 = encryption_dict[decrypted]
        found_keys = (key1, padded_key2)
        print(f"Keys found: Key1 = {key1.decode().strip()}, Key2 = {key2.decode().strip()}")
        break


if found_keys:
    key1, key2 = found_keys
    cipher2 = DES.new(key2, DES.MODE_ECB)
    intermediate_decrypted = cipher2.decrypt(encrypted_flag)
    cipher1 = DES.new(key1, DES.MODE_ECB)
    decrypted_flag = cipher1.decrypt(intermediate_decrypted)
    print(f"Decrypted flag: {decrypted_flag.decode().strip()}")
else:
    print("Keys not found.")

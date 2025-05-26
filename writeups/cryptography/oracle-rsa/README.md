Description
Can you abuse the oracle?
An attacker was able to intercept communications between a bank and a fintech company. They managed to get the message (ciphertext) and the password that was used to encrypt the message.
Additional details will be available after launching your challenge instance.

HINTS:
Crytography Threat models: chosen plaintext attack.
OpenSSL can be used to decrypt the message. e.g openssl enc -aes-256-cbc -d ...
The key to getting the flag is by sending a custom message to the server by taking advantage of the RSA encryption algorithm.
Minimum requirements for a useful cryptosystem is CPA security.


![Screenshot (101)](https://github.com/user-attachments/assets/8b71d626-2154-483f-8c90-cf6e01c955d4)


## Challenge: Oracle RSA

I was able to use the RSA multiplicative property to recover the plaintext of the encrypted password. However,
I couldn't complete the challenge because I wasn't sure how the recovered password was used to encrypt the secret message.
The password I got was only 6 bytes long, but the encryption method (AES-256-CBC) needs a 32-byte key.
I tried different ways to use the password—like padding it, treating it as a passphrase, 
and testing different OpenSSL options—but each time the decryption failed or gave unreadable output. Without knowing exactly how the key was created or if there was an IV used, I couldn’t decrypt the message and find the flag.

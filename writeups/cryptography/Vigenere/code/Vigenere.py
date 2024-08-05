def Vigenere(file_name:str, key:str) -> str:
    with open(file_name, 'r') as f:
        cipher = f.read()
    print("===============================================")
    print(f'The cipher text is: cipher = {cipher[:-1]}', end='\n\n')
    key:str = key.upper()
    key_len:int = len(key)

    decrypted_text:list = []

    i:int = 0
    while i < len(cipher):
        for k in range(key_len):
            while i+k < len(cipher) and not cipher[i+k].isalpha():
                decrypted_text.append(cipher[i+k])
                i += 1

            if i+k >= len(cipher):
                break

            decrypted_text.append(chr((ord(cipher[i+k].upper()) - ord(key[k]) + 26) % 26 + ord('A')))
            if cipher[i+k].islower():
                decrypted_text[-1] = decrypted_text[-1].lower()

        i += key_len
    
    print(f'The decrypted text is: decrypted_text = {"".join(decrypted_text)}')
    print("===============================================", end='\n\n')
    return "".join(decrypted_text)


if __name__ == '__main__':
    key = "CYLAB"
    file_name = "cipher.txt"

    try:
        decrypted_text = Vigenere(file_name, key)
        print(decrypted_text)
    except ValueError as e:
        print(e)



alphabet =['A','B','C','D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # list of alphabet
ENCRYPTION_INDEX =[] # list of encryption letter

def encrypt(key="", text=""):
    
    s = ""

    for i in text:
        index = alphabet.index(i)
        s += ENCRYPTION_INDEX[index]

    print(s)

def decrypt(key="", text=""):
    s=""
    for i in text:
        index = ENCRYPTION_INDEX.index(i)
        s+= alphabet[index]

    print(s)




if __name__ == "__main__":
    print("This is Keyword Cipher. A form of monoalphabetic substitution")

    keyword = input('Enter the keyword: ').upper()
    plaintext = input('Enter the message to encrypt/decrypt: ').upper()
    action = input('Enter E for encryption and D for decryption: ').upper()


    for i in keyword:
        if i not in ENCRYPTION_INDEX:
            ENCRYPTION_INDEX.append(i)

    for i in alphabet:
        if i not in ENCRYPTION_INDEX:
            ENCRYPTION_INDEX.append(i)


    if action == 'E':
        encrypt(keyword, plaintext)
    
    if action == 'D':
        decrypt(keyword, plaintext)

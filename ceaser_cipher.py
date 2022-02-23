'''This is project on Ceaser Cipher. A simple data encryption technique'''

from curses.ascii import isupper


def encrypt(str, shift):
    print(f'The encryption of "{str}" is:')
    S = ""
    for i in str:
        if i.isupper():
            S += chr((ord(i) + shift - 65) % 26 + 65)

    #   Logic behind the line:
    #   let i == 'Z' then index = ord(i)+2-65 = 25
    #   now 27 + 65 = 92 which in unicode is '\'
    #   therefore to correct it we take divide the index by 26(as there are 26 letter in English) and take the quotient and then add 65 to it.
    #    Same logic for lowercase letters as well
        if i.islower():
            S += chr((ord(i) + shift - 97) % 26 + 97)

    print(S)


def decrypt(str, shift):
    print(f'The decryption of "{str}" is:')
    S = ""
    for i in str:
        if i.isupper():
            index = ord(i) - shift
            if index < 65:
                index = 90 - (65 - index) + 1
            S += chr(index)
        if i.islower():
            index = ord(i) - shift
            if index < 97:
                index = 122 - (97 - index) + 1
            S += chr(index)
    print(S)


if __name__ == "__main__":
    print(
        "This is project on Ceaser Cipher. A simple data encryption technique."
    )
    print(
        "Enter 'E' before the string, if you want to encode a string or Enter 'D' before the string, if you want to decode it."
    )

    s = input("Enter the string:")
    shift = int(input("Enter shift value:"))
    if s != '' and shift != 0:
        if s[0] == 'E':
            encrypt(s[1:], shift)
        if s[0] == 'D':
            decrypt(s[1:], shift)
#!/usr/bin/python3

def main():
    message = input("Enter a message: ").upper()
    key = int(input('Enter your key:' ))
    # Make sure key is not greater than the number of letters
    if key > 25:
        key = key % 26
    mode = mode_fn()
    if mode == 1:
        print(encrypt_caesar(message, key))
    elif mode == 2:
        print(decrypt_caesar(message, key))

def encrypt_caesar(message, key):
    translated = ''
    for m in message:
        if m in LETTERS:
            num = LETTERS.find(m)
            num = (num + key)
            if num > 25:
                num = num % 26
            translated += LETTERS[num]
        else:
            # If there is a special character, just add it..
            translated += m

    return translated

def decrypt_caesar(message, key):
    translated = ''
    for m in message:
        if m in LETTERS:
            num = LETTERS.find(m)
            num = num - key
            if num < 0:
                num = num +len(LETTERS)
            translated += LETTERS[num]
        else:
            # If there is a special character, just add it..
            translated += m
    return translated

def mode_fn():
    ans = int(input("choose '1' to encrypt and '2' to decrypt '0' to exit: "))
    while ans not in [0, 1, 2]:
        ans = int(input('choose 1 to encrypt and 2 to decrypt: '))
    if ans == 0:
        exit()
    return ans


    
if __name__ == '__main__':
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    main()



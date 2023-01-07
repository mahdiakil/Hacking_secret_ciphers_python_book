#!/usr/bin/python3

def mode_fn():
    ans = int(input("choose '1' to encrypt and '2' to decrypt '0' to exit: "))
    while ans not in [0, 1, 2]:
        ans = int(input('choose 1 to encrypt and 2 to decrypt: '))
    if ans == 0:
        exit()
    return ans


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Enter a message: ").upper()
key = int(input('Enter your key:' ))
if key > 25:
    key = key % 26

mode = mode_fn()
translated = ''

for m in message:
    if m in LETTERS:
        num = LETTERS.find(m)
        if mode == 1:
            num = (num + key)
            if num > 25:
                num = num % 26
            translated += LETTERS[num]
        elif mode == 2:
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated += LETTERS[num]
    else:
        translated += m

print(f"translated: {translated}")
    




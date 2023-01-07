#!/usr/bin/python3

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Enter a message: ").upper()
i = 0
translate = ''
while i < 26:
    for m in message:
        if m in LETTERS:
            loc = LETTERS.find(m)
            new_loc = loc - i
            if new_loc < 0:
                new_loc = new_loc + len(LETTERS)
            translate += LETTERS[new_loc]
        else:
            translate += m
    print(f"Key {i}: {translate}")
    translate = ''
    i += 1        



#!/usr/bin/python3

message = input("Enter a message a encrypt or decrypt: ")
new_message = ""

i = len(message) -1

while i >= 0:
    new_message = new_message + message[i]
    i = i -1

print(new_message)

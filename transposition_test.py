#!/usr/bin/python3

import random, sys, transposition_cipher

def main():
    random.seed(42)

    for i in range(20):
        #Generate random messages to test
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'* random.randint(4, 40)

        #conver the message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)

        message = ''.join(message)
        print(f"Test: {i+1}, {message[:50]}")
        
        #Check all possible keys for each message
        for key in range(1, len(message)):
            encrypted = transposition_cipher.encrypt_text(message, key)
            decrypted = transposition_cipher.decrypt_cipher(encrypted, key)

            # If decryption doesn't match original message, display an error message and quit.
            if message != decrypted:
                print(f"Mismatch with {key} and message {message}")
                print(decrypted)
                sys.exit()

        print("Transposition cipher test passed!")

if __name__ == '__main__':
    main()

# Note that: each line of code written here could be written in a hundred ways better than this 'I AM BAD AT PYTHON!'

## This repo is used by me to improve my python and cryptography 'skills'

## Hacking Secret Ciphers With Python Book by Al Sweigart [book link](https://inventwithpython.com/cracking/ "book")

### In this repo I will try to solve all the exercises from the book above.

### Most solution will be mine but of course some will be from the book as well.

### I tried to make the solutions as general as possibe

## repo contents:
1. Caesar_cipher.py
	* Asks user for a msg, a key, and a mode (encrypt/decrypt)
	* Contains an encryption fn, decryption fn and a mode fn which lets users choose to encrypt or decrypt or exit.
2. hacking_caesar_cipher.py
	* Brute forces all keys (0-26) and prints the result of each key
3. transposition_cipher.py
	* Asks user for a msg, a key, and a mode (encrypt/decrypt)
	* Contains an encryption fn, decryption fn and calls the mode_fn from caesar_cipher file.
4. transposition_test.py
	* Creats random strings and tests the encryption and decryption of the transposition_cipher.py
5. transposition_file_cipher.py
	* Reads a txt file and uses the fns from the transposition_cipher (encryption and decryption) to either encrypt or decrypt the file
	* A user needs to provide a path for the txt file to encrypt/decrypt
6. detect_english.py and dictionary.txt
	* loads a dictionary and returns the percentage of english words and letters in a given message
7. hack_transposition_cipher.py
	* Given an encrypted message (hard coded), one can try all the keys from 1 till the len(message) and checks if the result is in english using the detect_english.py.
8. crypto_math.py
	* Includes fns that will be used such as finding gcd and modular inverse of 2 numbers
9. affine_cipher.py
	* a multiplicative cipher, uses crypto_math.py
10. affine_key_test.py
	* a program to test the keyspace of affine cipher which adds up to 7125 possible keys only!

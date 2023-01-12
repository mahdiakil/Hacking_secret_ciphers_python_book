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
11. hacking_affine_cipher.py
	* a program to hack the affine cipher, need to have a proper message.. (this cshould be improved)
12. substitution_cipher.py
	* a program that uses the substitution_cipher (could be improved to let the user add their own message or keys?)
13. make_word_pattern.py
	* this program uses dictionary.txt in order to create another python file 'word_pattern.py' which creates patterns for all the words in the dictionary and puts them in a dictionary. Som later we can call 'word_pattern.all_patterns['0.1.2.1.1.3.4']' which will print all the words of that has the pattern '0.1.2.1.1.3.4'

## You want to contribute?
Please do!

## Who do I talk to?
Mahdi Akil, Phd student at Karlstad University, Sweden. Reach me on mahdi.akil@kau.se

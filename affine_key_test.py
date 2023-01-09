# This program proves that the keyspace of the affine cipher is limited to len(SYMBOLS) ^ 2

import affine_cipher, crypto_math

message = "Make things as simple as possible, but not simpler"
for key_A in range(2,100):
    key = key_A * len(affine_cipher.SYMBOLS) + 1

    if crypto_math.gcd(key_A, len(affine_cipher.SYMBOLS)) == 1:
        print(key_A, affine_cipher.encrypt_message(message, key))

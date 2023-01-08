import sys, crypto_math, caesar_cipher, random

# len(SYMBOLS 96)
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front

#SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
#    my_message = """"A computer would deserve to be called intelligent if it
#could deceive a human into believing that it was human." -Alan Turing"""
    my_mode = caesar_cipher.mode_fn()
    my_message = input("Write a message to encrypt/decrypt: ")
    my_key = int(input("add a key: "))


    if my_mode == 1:
        translated = encrypt_message(my_message, my_key)
    elif my_mode == 2:
        translated = decrypt_cipher(my_message, my_key)
    print(f"Key: {my_key}")
    print(translated)

def get_key_parts(key):
    key_A = key // len(SYMBOLS)
    key_B = key % len(SYMBOLS)
    return (key_A, key_B)

def check_keys(key_A, key_B, mode):
    if key_A == 1 and mode == 1:
        sys.exit("The affine cipher becomes incredebly weak when key A is set to 1. Choose a different key.")
    if key_B == 0 and mode == 1:
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if key_A < 0 or key_B < 0 or key_B > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if crypto_math.gcd(key_A, len(SYMBOLS)) != 1:
        sys.exit(f"Key A {key_A} and the symbol set size {len(SYMBOLS)} are not relatively prime. Choose a different key.")


def encrypt_message(message, key):
    key_A, key_B = get_key_parts(key)
    check_keys(key_A, key_B, 1)
    cipher_text = '' 
    for m in message:
        if m in SYMBOLS:
            m_index = SYMBOLS.find(m)
            cipher_text += SYMBOLS[(m_index * key_A + key_B) % len(SYMBOLS)]
        else:
            cipher_text += m
    return cipher_text

def decrypt_cipher(message, key):
    key_A, key_B = get_key_parts(key)
    check_keys(key_A, key_B, 2)
    plain_text = ''
    mod_inverse_key_A = crypto_math.find_mode_inverse(key_A, len(SYMBOLS))

    for m in message:
        if m in SYMBOLS:
            m_index = SYMBOLS.find(m)
            plain_text += SYMBOLS[(m_index - key_B) * mod_inverse_key_A % len(SYMBOLS)]
        else:
            plain_text += m
    return plain_text

def get_random_keys():
    while True:
        key_A = random.randint(2, len(SYMBOLS))
        key_B = random.randint(2, len(SYMBOLS))
        if crypto_math.gcd(key_A, len(SYMBOLS)) == 1:
            return key_A * len(SYMBOLS) + key_B

if __name__ == '__main__':
    main()


import affine_cipher, detect_english, crypto_math

SILENT_MODE = False

def main():
    my_message = "U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"
    hacked_message = hack_affine(my_message)

    if hacked_message != None:
        print(hacked_message)
    else:
        print("Failed to hack the encryption.")

def hack_affine(message):
    print('Hacking...')
    print('Press cmd-c or cmd-d to quit at any time.')

    # for key in range(len(affine_cipher.SYMBOLS) ** 2):
    for key in range(3000):
        # print(key)
        key_A = affine_cipher.get_key_parts(key)[0]
        # print(key_A)
        if crypto_math.gcd(key_A, len(affine_cipher.SYMBOLS)) != 1:
            continue

        decrypted_text = affine_cipher.decrypt_cipher(message, key)
        if not SILENT_MODE:
            print(f'Tried key {key}...{decrypted_text[:40]}')

        if detect_english.is_english(decrypted_text):
            print()
            print('Possibe encryption hack: ')
            print(f"key: {key}")
            print(f"Decrypted message: {decrypted_text[:200]}")
            print()
            response = input("Enter D for done, or just press Enter to continue hacking..")

            if response.strip().upper().startswith('D'):
                return decrypted_text
    return None


if __name__ == '__main__':
    main()

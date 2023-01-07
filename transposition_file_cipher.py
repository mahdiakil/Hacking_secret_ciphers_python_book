import time, os, sys, caesar_cipher, transposition_cipher

def main():
    mode = caesar_cipher.mode_fn()
    file_name = input("Enter the full file name: ")
    if mode == 1:
        resulted_file = f"{file_name.removesuffix('.txt')}.encrypted.txt"
    elif mode == 2:
        resulted_file = f"{file_name.removesuffix('.txt')}.decrypted.txt"
    key = int(input("Enter a key: "))

    if not os.path.exists(file_name):
        print(f"The file {file_name} doesn't exist. Quitting...")
        sys.exit()

    if os.path.exists(resulted_file):
        print(f"This will overwrite the file {resulted_file}. (C)ontinue or (Q)uit?")
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    file_obj = open(file_name)
    content = file_obj.read()
    file_obj.close()


    start_time = time.time()
    
    if mode == 1:
        mode = 'encrypt'
        print(f"{mode.title()}ing...")
        translated = transposition_cipher.encrypt_text(content, key)
    elif mode == 2:
        mode = 'decrypt'
        print(f"{mode.title()}ing...")
        translated = transposition_cipher.decrypt_cipher(content, key)
    total_time = round(time.time() - start_time, 2)
    print(f"{mode.title()}ion time: {total_time} seconds")

    outpute_file_obj = open(resulted_file, 'w')
    outpute_file_obj.write(translated)
    outpute_file_obj.close()
    print(50*"#")
    print(f"Done {mode.title()}ing {file_name} with {len(content)} characters")
    print(f"{mode.title()}ed file is {resulted_file}")
    print(50*"#")

if __name__ == '__main__':
    main()
                                          

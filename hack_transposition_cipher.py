import detect_english, transposition_cipher

def main():

    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hacked_message = hack_transposition(myMessage)

    if hacked_message == None:
        print("failed to hack encryption.")
    else:
        print(hacked_message)

def hack_transposition(message):
    print("Hacking...")

    print("Press ctrl-c or ctrl-d to quit at any time..")

    for key in range(1, len(message)):
        print(f'trying key #{key}..')

        decrypted_text = transposition_cipher.decrypt_cipher(message, key)
        if detect_english.is_english(decrypted_text):
            print()
            print('Possible encryption hack:')
            print(f"Key {key}: {decrypted_text[:100]}")
            print()
            
            response = input("Enter D for done, or just press Enter to continue hacking: ")
            if response.strip().upper().startswith('D'):
                return decrypted_text
    return None

if __name__ == '__main__':
    main()



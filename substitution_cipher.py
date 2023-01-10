import sys, random

LETTERS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even o lightest evidence. The origin of myths is explained in this way. -Bertrand Russell'

    myKey = r"""/{9@6hUf:q?_)^eTi|W1,NLD7xk(-SF>Iz0E=d;Bu#c]w~'VvHKmpJ+}s8y& XtP43.b[OA!*\Q<M%$ZgG52YloaRCn"`rj"""

    myMode = 'encrypt'

    check_valid_key(myKey)

    if myMode == 'encrypt':
        translated = encrypt_message(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decrypt_message(myMessage, myKey)

    print(f'Using key {myKey}')
    print(f"The {myMode}ed message is:")
    print(translated)


def check_valid_key(key):
    key_list = list(key)
    letter_list = list(LETTERS)
    key_list.sort()
    letter_list.sort()
    if key_list != letter_list:
        sys.exit("There is an error in the key or letter set.")

def encrypt_message(message, key):
    return translate_message(message, key, 'encrypt')

def decrypt_message(message, key):
    return translate_message(message, key, 'decrypt')

def translate_message(message, key, mode):
    translated = ''
    chars_A = LETTERS
    chars_B = key

    if mode == 'decrypt':
        chars_A, chars_B = chars_B, chars_A

    for m in message:
        if m in chars_A:
            m_index = chars_A.find(m)
            translated += chars_B[m_index]
        else:
            translated += m

    return translated

def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()

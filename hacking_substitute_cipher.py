import os, re, copy, pprint, substitution_cipher, make_word_patterns

if not os.path.exists('word_pattern.py'):
    make_word_patterns.main()
import word_pattern

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
non_letters_or_space_patters = re.compile('[^A-Z\s]')

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    # Determine the possible valid ciphertext translations.
    print('Hacking...')
    letter_mapping = hack_simple_substitute(message)

    # Display the results to the user.
    print('Mapping:')
    pprint.pprint(letter_mapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('printing hacked message:')
    hacked_message = decrypt_with_cipher_letter_mapping(message, letter_mapping)
    print(hacked_message)

def get_blank_cipher_letter_mapping():
    # Returns a dictionary value that is a blank cipher letter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P':
[], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],
'Y': [], 'Z': []}

def add_letters_to_mapping(letter_mapping, cipher_word, candidate):
    # The letter_mapping parameter is a "ciper_letter mapping" dictionary
    # value that the return value of this fn starts as a copy of.
    # The cipher_word parameter is a string value of the ciphertext word.
    # The candidate parameter is a possible English word that the cipher_word would decrypt to.

    # This fn adds the letters of the candidate as potential decryption letters
    # or the cipherLetters in the cipherletter mapping.

    letter_mapping = copy.deepcopy(letter_mapping)
    for i in range(len(cipher_word)):
        if candidate[i] not in letter_mapping[cipher_word[i]]:
            print(candidate[i])
            letter_mapping[cipher_word[i]].append(candidate[i])
    return letter_mapping

def intersect_mapping(map_A, map_B):
    # To intersect two maps, create a blank map, and then add only the potential
    # decryption letters if they exist in BOTH maps.

    intersected_mapping = get_blank_cipher_letter_mapping()
    for letter in LETTERS:
        # An empty list means "any letter is possible". In this case just copy
        # the other map entirely.
        if map_A[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(map_B[letter])
        elif map_B[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(map_A[letter])
        else:
            # If a letter is map_A[letter] exits in map_B[letter], add that letter
            # to intersected_mapping[letter].
            for mapped_letter in map_A[letter]:
                if mapped_letter in map_B[letter]:
                    intersected_mapping[letter].append(mapped_letter)

    return intersected_mapping

def remove_solve_letters_from_mapping(letter_mapping):
    # Cipher letters in the mapping that map to only one letter are "solved" and can be 
    # removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B' maps to ['N'], then
    # we know that 'B' must map to 'N', so we can remove 'N' from the list of what 'A' could
    # map to. So 'A'  then maps to '[M]'. Note that now that 'A' maps to only one letter, we
    # can remove 'M' from the list of letters for every other letter. (This is why there is a loop
    # that keeps reducing the map.)
    letter_mapping = copy.deepcopy(letter_mapping)
    loop_again = True
    while loop_again:
        # First assume that we will not loop again:
        loop_again = False

        # solved letters will be a list of uppercase letters that have one and only one possible
        # mapping in letter_mapping
        solved_letters = []
        for ciper_letter in LETTERS:
            if len(letter_mapping[ciper_letter]) == 1:
                solved_letters.append(letter_mapping[ciper_letter][0])
        
        # If a letter is solved, then it cannot possibly be a potential decryption letter for a 
        # different ciphertext letter, so we should remove it from those other lists
        for ciper_letter in LETTERS:
            for s in solved_letters:
                if len(mapped_letter[ciper_letter]) != 1 and s in letter_mapping[ciper_letter]:
                    letter_mapping[ciper_letter].remove(s)
                    if len(letter_mapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again
                        loop_again = True

        return letter_mapping

def hack_simple_substitute(message):
    intersected_map = get_blank_cipher_letter_mapping()
    cipher_word_list = non_letters_or_space_patters.sub('', message.upper()).split()
    for cipher_word in cipher_word_list:
        # Get a new cipherletter mapping for each ciphertext word.
        new_map = get_blank_cipher_letter_mapping()

        word_patterns = make_word_patterns.get_word_pattern(cipher_word)
        if word_patterns not in word_pattern.all_patterns:
            continue # This word was not in our dictionary, so continue.

        # Add the letters for each candidate to the mapping.
        for candidate in word_pattern.all_patterns[word_patterns]:
            new_map = add_letters_to_mapping(new_map, cipher_word, candidate)

    # Remove any solved letters from the other lists.
    return remove_solve_letters_from_mapping(intersected_map)

def decrypt_with_cipher_letter_mapping(cipher_text, letter_mapping):
    # Return a string of the cipher_text decrypted with the letter mapping, with any 
    # ambiguous decrypted letters replaced with an '_' underscorse character.

    # First create a simple substitution key from the letter_mapping mapping.
    key = ['x'] * len(LETTERS)
    for cipher_letter in LETTERS:
        if len(letter_mapping[cipher_letter]) == 1:
            # If there is only one letter, add it to the key.
            key_index = LETTERS.find(letter_mapping[cipher_letter][0])
            key[key_index] = cipher_letter
        else:
            cipher_text = cipher_text.replace(cipher_letter.lower(), '_')
            cipher_text = cipher_text.replace(cipher_letter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the cipher_text.
    return substitution_cipher.decrypt_message(cipher_text, key)

if __name__ == '__main__':
    main()


import pprint

def get_word_pattern(word):
    # Return a string of the pattern form of the given word.
    # e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSBUSTER'
    word = word.upper()
    next_num = 0
    letter_num = {}
    word_pattern = []

    for letter in word:
        if letter not in letter_num:
            letter_num[letter] = str(next_num)
            next_num += 1
        word_pattern.append(letter_num[letter])
    return '.'.join(word_pattern)

def main():
    all_patterns = {}

    with open('dictionary.txt', 'r') as f:
        word_list = f.read().split('\n')

    for word in word_list:
        # Get the pattern for each string in word_list
        pattern = get_word_pattern(word)

        if pattern not in all_patterns:
            all_patterns[pattern] = [word]
        else:
            all_patterns[pattern].append(word)

    # This is code that writes code. The word_pattern.py file contains one
    # very, very large assignment statement

    with open('word_pattern.py', 'w') as fo:
        fo.write('all_patterns = ')
        fo.write(pprint.pformat(all_patterns))

if __name__ == '__main__':
    main()

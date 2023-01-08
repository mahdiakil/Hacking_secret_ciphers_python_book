# To use, type this code:
    # import detectEnglish
# detectEnglish.isEnglish(someString) # returns True or False
# (There must be a "dictionary.txt" file in this directory with all English 8. # words in it, one word per line. You can download this from
# http://invpy.com/dictionary.txt)


UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACES = UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n'


def load_dictionary():
    with open('dictionary.txt', 'r') as dictionary_file:
        english_words = dictionary_file.read().split('\n')

    return english_words

ENGLISH_WORDS = load_dictionary()

def remove_non_letters(message):
    letters_only = []
    for m in message:
        if m in LETTERS_AND_SPACES:
            letters_only += m
    return ''.join(letters_only)


def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()
    if possible_words == []:
        return 0.0

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)

def is_english(message, word_percentage = 20, letter_percentage = 85):
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match

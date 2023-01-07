#!/usr/bin/python3

import math

def main():
    mode = mode_fn()
    message = input("Type a message to encrypt or decrypt: ")
    key = int(input("Put the key: "))

    if mode == 1:
        print(f"{encrypt_text(message, key)}***")
        print("The message ended at '***'")
    else:
        print(f"decrypt_cipher(message, key)***")
        print("The message ended at '***'")




def mode_fn():
    ans = int(input("Choose '1' to encrypt, '2' to decrypt, and '0' to exit: "))
    while ans not in [0, 1, 2]:
        ans = int(input("Choose '1' to encrypt, '2' to decrypt, and '0' to exit: "))
    if ans == 0:
        exit()
    return ans

def split_list(input_list, k):
    # Get the length of the input list
    n = len(input_list)
    # Divide the length by k to get the number of sublists
    num_sublists = n // k
    # Initialize a new list to hold the sublists
    sublists = []
    # Iterate over the range of sublists
    for i in range(num_sublists):
        # Get the start and end indices for the current sublist
        start = i * k
        end = (i + 1) * k
        # Get the current sublist and append it to the list of sublists
        sublist = input_list[start:end]
        sublists.append(sublist)
    # Check if there is a remainder
    if n % k != 0:
        # Get the remaining elements and append them to a new sublist
        remainder = input_list[num_sublists * k:]
        # Pad the remainder sublist with spaces until it has size k
        while len(remainder) < k:
            remainder.append('')
        # Append the remainder sublist to the list of sublists
        sublists.append(remainder)
    # Return the list of sublists
    return sublists

def decrypt_cipher(message, key):
    col_needed = math.ceil((len(message)/key))
    rows_needed = key
    shaded_boxes = (col_needed * rows_needed) - len(message)
    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * col_needed
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        # If there are no more columns OR we are at a shaded box,
        # go back to the first column and the next row
        if (col == col_needed) or (col == col_needed - 1 and row >= rows_needed - shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

def encrypt_text(message, key):
    list_of_chars = []
    new_list= []
    i = 0
    for m in message:
        list_of_chars.append(m)
        new_list = split_list(list_of_chars, key)

    enc_list = ""
    j =0
    while j < key:
        for i in range(len(new_list)):
            enc_list += new_list[i][j]
        j += 1    
    return enc_list

if __name__ == '__main__':
    main()



from math import floor
from art import logo
import string
alphabet = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
alphabet.append(' ')
alphabet += alphabet
encoder = True

def main():
    encoder = True
    while encoder:
        direction = ""
        shift = ""
        while direction == "":
            try:
                direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()[0]
                if direction == "d":
                    direction = "decoded"
                    continue
                elif direction == "e":
                    direction = "encoded"
                    continue
                else:
                    raise IndexError
            except IndexError:
                print("Please enter 'encode' or 'decode'.")
                direction = ""
        text = input("Type your message:\n")
        while shift == "":
            try:
                shift = int(input("Type the shift number:\n"))
                shift =  int(shift % (len(alphabet)/2))
                message = caesar_cipher(encrypt=direction, text=text, shift=shift)
                print(f"The {direction} text is:{''.join(message)}\n")
                encoder = quit()
            except ValueError:
                print("Please put in a valid integer.")
                shift = True

def quit():
    keep_going = input("Would you like to use it again? (Y/N)\n").lower()[0]
    if keep_going == "n":
        print("Thank you for using the Caesar Cipher encoder/decoder.")
        return False
    else:
        return True

def caesar_cipher(encrypt, text, shift):
    text_list = list(text)
    if encrypt == "decoded":
        shift *= -1
    for char in range(len(text_list)):
        if text_list[char] in alphabet:
            text_list[char] = alphabet.index(text_list[char]) + shift
            text_list[char] = alphabet[text_list[char]]
    return text_list

if __name__ == "__main__":
    print(logo)
    main()

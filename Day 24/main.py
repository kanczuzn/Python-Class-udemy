PLACEHOLDER = "[name]"


def main():
    with open("./Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
    with open("./Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.read()

    for name in names:
        new_letter = letter.replace(PLACEHOLDER, name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as fin_letter:
            fin_letter.write(new_letter)


if __name__ == "__main__":
    main()

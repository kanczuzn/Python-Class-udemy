import pandas

def main():
    imported = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter: row.code for (index, row) in imported.iterrows()}

    word = input("What would you like translated? ").strip().upper()
    result = [phonetic_dict[letter] if letter in phonetic_dict else letter for letter in word]
    print(result)


if __name__ == "__main__":
    main()

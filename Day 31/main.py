from tkinter import *
from random import choice
import pandas
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_CARD = ("Ariel", 60, "bold")


def main():
    # Word List
    try:
        word_file = pandas.read_csv("./data/word_list.csv")
    except FileNotFoundError:
        messagebox.showerror(title="Oh no!", message="The word list cannot be found!")
    else:
        lang_1 = word_file.columns[0]
        lang_2 = word_file.columns[1]
        word_list = word_file.to_dict(orient="records")

    # Unknown Word
    def unknown_word():
        current_card = choice(word_list)
        canvas.itemconfig(card_lang, text=lang_1)
        canvas.itemconfig(card_word, text=current_card[lang_1])

    # UI Initialization
    window = Tk()
    window.title("Flashy!")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_front_img = PhotoImage(file="./images/card_front.png")
    card_back_img = PhotoImage(file="./images/card_back.png")
    wrong_img = PhotoImage(file="./images/wrong.png")
    correct_img = PhotoImage(file="./images/right.png")
    canvas.create_image(400, 263, image=card_front_img)

    # Buttons & Tags
    card_lang = canvas.create_text(400, 130, text="", font=FONT_TITLE, tags='language')
    card_word = canvas.create_text(400, 263, text="", font=FONT_CARD, tags='word')
    wrong_button = Button(image=wrong_img, highlightthickness=0, command=unknown_word)
    correct_button = Button(image=correct_img, highlightthickness=0)

    # Layout
    canvas.grid(row=1, column=1, columnspan=2)
    correct_button.grid(row=2, column=2)
    wrong_button.grid(row=2, column=1)


    unknown_word()
    window.mainloop()


if __name__ == "__main__":
    main()

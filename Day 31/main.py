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
        try:
            word_file = pandas.read_csv('./data/words_to_learn.csv')
        except FileNotFoundError:
            word_file = pandas.read_csv("./data/word_list.csv")
    except FileNotFoundError:
        messagebox.showerror(title="Oh no!", message="The word list cannot be found!")
    else:
        lang_1 = word_file.columns[0]
        lang_2 = word_file.columns[1]
        word_list = word_file.to_dict(orient="records")
        current_card = {}

    # Word is known
    def known_word():
        nonlocal word_list
        if len(word_list) >= 1:
            word_list.remove(current_card)
        new_word()

    # Unknown Word
    def new_word():
        nonlocal current_card, flip_timer, word_list
        window.after_cancel(flip_timer)
        if len(word_list) >= 1:
            current_card = choice(word_list)
            canvas.itemconfig(card_bg, image=card_front_img)
            canvas.itemconfig(card_lang, text=lang_1, fill="black")
            canvas.itemconfig(card_word, text=current_card[lang_1], fill="black")
            flip_timer = window.after(3000, func=flip_card)
        else:
            canvas.itemconfig(card_bg, image=card_back_img)
            canvas.itemconfig(card_lang, text="", fill="white")
            canvas.itemconfig(card_word, text="No More Cards!", fill="white")
            messagebox.showinfo(title="Congratulations!", message="🎉🎉🎉 You knew all the words! 🎉🎉🎉\n"
                                                                  "     Way to go! Find some new ones.")

    # Change card
    def flip_card():
        canvas.itemconfig(card_bg, image=card_back_img)
        canvas.itemconfig(card_lang, text=lang_2, fill="white")
        canvas.itemconfig(card_word, text=current_card[lang_2], fill="white")

    # Save File
    def save_file():
        if len(word_list) >= 1:
            if messagebox.askyesno(title="Goodbye!", message="Would you like to update your \n"
                                                             "saved words based on the session?"):
                words_to_learn = pandas.DataFrame(word_list)
                words_to_learn.to_csv('./data/words_to_learn.csv', index=False)
            else:
                pass
        window.destroy()

    # UI Initialization
    window = Tk()
    window.title("Flashy!")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_front_img = PhotoImage(file="./images/card_front.png")
    card_back_img = PhotoImage(file="./images/card_back.png")
    wrong_img = PhotoImage(file="./images/wrong.png")
    correct_img = PhotoImage(file="./images/right.png")
    card_bg = canvas.create_image(400, 263, image=card_back_img)

    # Buttons & Tags
    card_lang = canvas.create_text(400, 130, text="", font=FONT_TITLE, tags='language')
    card_word = canvas.create_text(400, 263, text="", font=FONT_CARD, tags='word')
    wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
    correct_button = Button(image=correct_img, highlightthickness=0, command=known_word)

    # Layout & Final Initialization
    flip_timer = window.after(3000, func=flip_card)
    new_word()
    canvas.grid(row=1, column=1, columnspan=2)
    correct_button.grid(row=2, column=2)
    wrong_button.grid(row=2, column=1)

    window.protocol("WM_DELETE_WINDOW", save_file)
    window.mainloop()


if __name__ == "__main__":
    main()

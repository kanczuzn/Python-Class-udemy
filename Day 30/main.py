from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json

WHITE = "#ffffff"
FONT = ("Courier", 10)


def main():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def rand_pass():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        pass_letters = [choice(letters) for _ in range(randint(8, 10))]
        pass_sym = [choice(symbols) for _ in range(randint(2, 4))]
        pass_num = [choice(numbers) for _ in range(randint(2, 4))]
        password_list = pass_letters + pass_sym + pass_num

        shuffle(password_list)
        password = "".join(password_list)
        pass_input.delete(0, END)
        pass_input.insert(0, password)
        copy(password)

    # ---------------------------- FIND ENTRY ---------------------------------- #
    def find_entry():
        website = web_input.get()
        if len(website) < 1:
            messagebox.showerror(title="Oops!", message="You didn't type in a website!")
        else:
            try:
                with open("data.json", "r") as pass_write:
                    data = json.load(pass_write)
                info = f"E-mail: {data[website]['email']}\n" \
                       f"Password: {data[website]['password']}"
            except FileNotFoundError:
                messagebox.showerror(title="Oops!", message="You don't have any passwords stored yet!")
            except KeyError:
                messagebox.showerror(title="Oops!", message="You don't have an entry for that yet!")
            else:
                messagebox.showinfo(title=website, message=info)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def add_entry():
        website = web_input.get()
        username = user_input.get()
        password = pass_input.get()
        new_data = {website: {
            "email": username,
            "password": password,
            }
        }
        if len(website) < 1 or len(username) < 1 or len(password) < 1:
            messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")
        else:
            data = new_data
            try:
                with open("data.json", "r") as pass_write:
                    data = json.load(pass_write)
                    data.update(new_data)
                try:
                    if data[website]['email'] == username:
                        messagebox.showerror(title="Oops!", message="You already have an entry for that!")
                except:
                    pass
            except FileNotFoundError:
                pass
            finally:
                with open("data.json", "w") as pass_write:
                    json.dump(data, pass_write, indent=4)
                    web_input.delete(0, END)
                    pass_input.delete(0, END)
                    web_input.focus()

    # ---------------------------- UI SETUP ------------------------------- #
    # Initial Window, Canvas, and Image
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg=WHITE)
    canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)

    # Labels, Entries, and Buttons
    web_title = Label(text="Website:", font=FONT, bg=WHITE)
    web_input = Entry(width=32, bg=WHITE)
    web_input.focus()
    search_button = Button(text="Search", font=FONT, highlightthickness=0, width=17, bg=WHITE, command=find_entry)
    user_title = Label(text="Email/Username:", font=FONT, bg=WHITE)
    user_input = Entry(width=58, bg=WHITE)
    try:
        with open("data.json", "r") as find_email:
            init_data = json.load(find_email)
            init_email = init_data[list(init_data)[-1]]['email']
            user_input.insert(END, init_email)
    except FileNotFoundError:
        pass
    pass_title = Label(text="Password:", font=FONT, bg=WHITE)
    pass_input = Entry(width=32, bg=WHITE)
    gen_pass_button = Button(text="Generate Password", font=FONT, highlightthickness=0, bg=WHITE, command=rand_pass)
    add_button = Button(text="Add", font=FONT, highlightthickness=0, width=43, bg=WHITE, command=add_entry)

    # Layout
    canvas.grid(row=1, column=1, columnspan=3)
    web_title.grid(row=2, column=1, sticky="E")
    web_input.grid(row=2, column=2, sticky="W")
    search_button.grid(row=2, column=3, sticky="E")
    user_title.grid(row=3, column=1, sticky="E")
    user_input.grid(row=3, column=2, columnspan=2, sticky="W")
    pass_title.grid(row=4, column=1, sticky="E")
    pass_input.grid(row=4, column=2, sticky="W")
    gen_pass_button.grid(row=4, column=3, sticky="E")
    add_button.grid(row=5, column=2, columnspan=2, sticky="W")

    # Window Stay Open
    window.mainloop()


if __name__ == "__main__":
    main()

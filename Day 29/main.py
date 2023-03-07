from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy

WHITE = "#ffffff"
FONT = ("Courier", 10)


def main():
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def rand_pass():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

# ---------------------------- SAVE PASSWORD ------------------------------- #
    def add_entry():
        website = web_input.get()
        username = user_input.get()
        password = pass_input.get()
        if len(website) < 1 or len(username) < 1 or len(password) < 1:
            messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
        else:
            new_entry = f"{website} | {username} | {password}\n"
            confirm_entry = messagebox.askyesno(title="Confirm Entry", message=f"These are the details entered:"
                                                                               f"\nWebsite: {website}"
                                                                               f"\nEmail: {username}"
                                                                               f"\nPassword: {password}"
                                                                               f"\nIs this correct?")
            print(confirm_entry)
            if confirm_entry == True:
                with open("password.txt", mode="a") as pass_write:
                    pass_write.write(new_entry)
                web_input.delete(0, END)
                pass_input.delete(0, END)
            web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg=WHITE)
    canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)

    #Labels, Entries, and Buttons
    web_title = Label(text="Website:", font=FONT, bg=WHITE)
    web_input = Entry(width=58, bg=WHITE)
    web_input.focus()
    user_title = Label(text="Email/Username:", font=FONT, bg=WHITE)
    user_input = Entry(width=58, bg=WHITE)
    pass_title = Label(text="Password:", font=FONT, bg=WHITE)
    pass_input = Entry(width=32, bg=WHITE)
    gen_pass_button = Button(text="Generate Password", font=FONT, highlightthickness=0, bg=WHITE, command=rand_pass)
    add_button = Button(text="Add", font=FONT, highlightthickness=0, width=43, bg=WHITE, command=add_entry)

    #Layout
    canvas.grid(row=1, column=1, columnspan=3)
    web_title.grid(row=2, column=1, sticky="E")
    web_input.grid(row=2, column=2, columnspan=2, sticky="W")
    user_title.grid(row=3, column=1, sticky="E")
    user_input.grid(row=3, column=2, columnspan=2, sticky="W")
    pass_title.grid(row=4, column=1, sticky="E")
    pass_input.grid(row=4, column=2, sticky="W")
    gen_pass_button.grid(row=4, column=3, sticky="E")
    add_button.grid(row=5, column=2, columnspan=2, sticky="W")

    #Window Stay Open
    window.mainloop()


if __name__ == "__main__":
    main()

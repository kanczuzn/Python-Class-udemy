from tkinter import *
import requests as req


# Eww, Kanye. I wouldn't make this on my own, but the class requested it.
def get_quote():
    pull_quote = req.get("https://api.kanye.rest")
    if pull_quote.status_code != 200:
        pull_quote.raise_for_status()
    else:
        new_quote = pull_quote.json()['quote']
        canvas.itemconfig(quote_text, text=new_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text="",
                                width=250,
                                font=("Arial", 30, "bold"),
                                fill="white")
get_quote()
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
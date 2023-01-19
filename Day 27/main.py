from tkinter import *


class Prox(Entry):

    def __init__(self, master=None, **kwargs):
        self.var = StringVar(master, value="0")
        self.var.trace('w', self.validate)
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set

    def validate(self):
        value = self.get().replace('.', "", 1)
        if not value.isdigit():
            self.set(''.join(x for x in value if x.isdigit()))


WINDOW = Tk()
FONT = ("Arial", 10)


def main():
    WINDOW.config(padx=75, pady=50)
    WINDOW.title("Miles to Kilometer Converter")
    which_conversion = IntVar(value=1)
    user_input = Prox(width=10)
    from_label = Label(text="Mi", font=FONT)
    to_label = Label(text="Km", font=FONT)

    def toggle_state():
        if which_conversion.get() == 1:
            WINDOW.title("Miles to Kilometer Converter")
            from_label.config(text="Mi")
            to_label.config(text="Km")
        else:
            WINDOW.title("Kilometer to Miles Converter")
            from_label.config(text="Km")
            to_label.config(text="Mi")

    def convert_to_result():
        x = float(user_input.get())
        if which_conversion.get() == 1:
            x *= 1.609344
        else:
            x *= 0.621377
        result_label.config(text=round(x, 3))

    mi_to_km_radio = Radiobutton(text="Mi to Km", value=1, variable=which_conversion, command=toggle_state)
    km_to_mi_radio = Radiobutton(text="Km to Mi", value=2, variable=which_conversion, command=toggle_state)
    result_label = Label(text="0", font=FONT)
    eq2_label = Label(text="is equal to", font=FONT)
    WINDOW.minsize(width=350, height=150)
    button = Button(text="Calculate", command=convert_to_result)
    user_input.grid(row=0, column=1)
    from_label.grid(row=0, column=2)
    eq2_label.grid(row=1, column=0)
    result_label.grid(row=1, column=1)
    to_label.grid(row=1, column=2)
    mi_to_km_radio.grid(row=1, column=3)
    button.grid(row=2, column=1)
    km_to_mi_radio.grid(row=2, column=3)


if __name__ == "__main__":
    main()
    WINDOW.mainloop()

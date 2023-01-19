from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
REPS = 1
TIMER = None


def main():
    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer():
        global TIMER
        global REPS
        if TIMER != None:
            window.after_cancel(TIMER)
            pom_label.config(text="Timer")
            canvas.itemconfig(timer_text, text="00:00")
            REPS = 1
            pom_check.config(text="")

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer():
        global REPS
        if REPS > 8:
            REPS = 1
        if REPS % 8 == 0:
            pom_label.config(text="Break", fg=RED)
            timer(LONG_BREAK_MIN)
        elif REPS % 2 == 0:
            timer(SHORT_BREAK_MIN)
            pom_label.config(text="Break", fg=PINK)
        else:
            pom_label.config(text="Work", fg=GREEN)
            timer(WORK_MIN)
        pom_check.config(text="✔" * math.floor(REPS / 2))
        REPS += 1

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def timer(count):
        global TIMER
        count_down = f"{math.floor(count / 60):02}:{count % 60:02}"
        canvas.itemconfig(timer_text, text=count_down)
        if count > 0:
            TIMER = window.after(1000, timer, count - 1)
        else:
            start_timer()

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)
    canvas = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
    pom_label = Label(text="Timer", font=(FONT_NAME, 38, "bold"), fg=GREEN, bg=YELLOW)
    button_start = Button(text="Start", font=FONT_NAME, bg=PINK, highlightthickness=0, command=start_timer)
    button_reset = Button(text="Reset", font=FONT_NAME, bg=PINK, highlightthickness=0, command=reset_timer)
    pom_check = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
    pom_label.grid(row=1, column=2)
    canvas.grid(row=2, column=2)
    button_start.grid(row=3, column=1)
    button_reset.grid(row=3, column=3)
    pom_check.grid(row=4, column=2)
    window.mainloop()


if __name__ == "__main__":
    main()

import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
import pixela_commands

BACKGROUND_COLOR_1 = "#dfe5ee"
BACKGROUND_COLOR_2 = "#25476a"
FONT = ("Helvetica", 12)
ERROR_FONT = ("Helvetica", 10, "italic")


class PixelaInterface:

    def __init__(self, user):
        # UI Initilization
        self.window = Tk()
        self.window.title("Unofficial pixela UI")
        self.window.config(bg=BACKGROUND_COLOR_1)
        self.canvas_head = Canvas(width=300, height=100, bg=BACKGROUND_COLOR_1, highlightthickness=0)
        with open("./img/pixela_color.png", "rb") as art:
            pixela_import = Image.open(art)
            pixela_resize = pixela_import.resize((147, 40), Image.Resampling.LANCZOS)
            pixela_img = ImageTk.PhotoImage(pixela_resize)
        self.canvas_head.create_image(84, 40, image=pixela_img)
        self.canvas_body = Canvas(width=300, height=400, bg=BACKGROUND_COLOR_2, highlightthickness=0)
        self.canvas_body_frame = Frame(borderwidth=0, width=100, height=250, bg=BACKGROUND_COLOR_2)
        self.user_error = Label(self.canvas_body_frame, fg="red", font=ERROR_FONT, bg=BACKGROUND_COLOR_2)
        self.user_msg = Label(self.canvas_body_frame, fg="white", font=ERROR_FONT, bg=BACKGROUND_COLOR_2)
        self.username = user
        self.graphs = list

        # Main UI
        self.canvas_head.grid(row=1, column=1, columnspan=3)
        self.canvas_body.grid(row=2, column=1, columnspan=3, rowspan=3)
        self.canvas_body_frame.grid(row=2, column=1, columnspan=3, pady=30)

        self.main_page()
        self.window.mainloop()

    # Main Page of the UI
    def main_page(self):
        self.clear_frame()
        create_graph = Button(self.canvas_body_frame, text="Create Graph",
                              font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                              command=self.new_graph)
        add_datapoint = Button(self.canvas_body_frame, text="Add Datapoint",
                               font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                               command=lambda: self.pick_graph("add"))
        modify_datapoint = Button(self.canvas_body_frame, text="Modify Datapoint",
                                  font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                  command=lambda: self.pick_graph("mod"))
        copy_label = Label(text="image copyright pixela https://pixe.la/",
                           fg="white",
                           bg=BACKGROUND_COLOR_2,
                           font=("Helvetica", 7, "italic"))
        if self.username == "New User":
            usr_label = Label(self.canvas_body_frame,
                              text="Create a User First.",
                              fg="white",
                              bg=BACKGROUND_COLOR_2,
                              font=FONT)
            new_usr_button = Button(self.canvas_body_frame, text=self.username,
                                    font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                    command=self.new_user)
            create_graph.config(state="disabled")
            add_datapoint.config(state="disabled")
            modify_datapoint.config(state="disabled")
        else:
            usr_label = Label(self.canvas_body_frame, text=f"Welcome back, \n{self.username}!",
                              fg="white",
                              bg=BACKGROUND_COLOR_2,
                              font=FONT)
            new_usr_button = Button()
            self.graphs = pixela_commands.graphs(self.username)

        # UI Layout
        copy_label.grid(row=4, column=1, sticky=SW)

        # UI Buttons inside Frame
        if self.username == "New User":
            usr_label.grid(row=0, column=2, sticky=NSEW)
            new_usr_button.grid(row=1, column=2, sticky=NSEW)
        else:
            usr_label.grid(row=0, column=2, sticky=NSEW, rowspan=2)
        create_graph.grid(row=2, column=2, sticky=NSEW)
        add_datapoint.grid(row=3, column=2, sticky=NSEW)
        modify_datapoint.grid(row=4, column=2, sticky=NSEW)

    # New User UI
    def new_user(self):
        self.clear_frame()
        if self.username == "New User":
            tos = BooleanVar(value=False)
            minor = BooleanVar(value=False)

            # Labels, Input, and Buttons
            usrname_label = Label(self.canvas_body_frame, text="Username:", fg="white",
                                  font=FONT, bg=BACKGROUND_COLOR_2)
            usrname_input = Entry(self.canvas_body_frame, bg="white")
            usrname_input.focus()
            apikey_label = Label(self.canvas_body_frame, text="API Key:", fg="white",
                                 font=FONT, bg=BACKGROUND_COLOR_2)
            apikey_input = Entry(self.canvas_body_frame, bg="white")
            tos_label = Label(self.canvas_body_frame, text="Do you agree to the TOS?", fg="white",
                              font=FONT, bg=BACKGROUND_COLOR_2)
            tos_check = Checkbutton(self.canvas_body_frame, bg=BACKGROUND_COLOR_2, variable=tos,
                                    onvalue=True, activebackground=BACKGROUND_COLOR_2)
            minor_label = Label(self.canvas_body_frame, text="Are you not a minor\n"
                                                             "or have consent?",
                                fg="white", font=FONT, bg=BACKGROUND_COLOR_2)
            minor_check = Checkbutton(self.canvas_body_frame, bg=BACKGROUND_COLOR_2, variable=minor,
                                      onvalue=True, activebackground=BACKGROUND_COLOR_2)
            new_usr_submit = Button(self.canvas_body_frame, text="Submit", font=FONT,
                                    highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                    command=lambda: self.submit_new(
                                        usrname_input.get().lower().strip(),
                                        apikey_input.get().strip(),
                                        tos.get(),
                                        minor.get()
                                    )
                                    )
            new_usr_back = Button(self.canvas_body_frame, text="Back", font=FONT,
                                  highlightthickness=0, bg=BACKGROUND_COLOR_1, command=self.main_page)

            # Grid Setup
            usrname_label.grid(row=1, column=1, sticky=W, columnspan=3)
            usrname_input.grid(row=2, column=1, stick=NSEW, columnspan=3)
            apikey_label.grid(row=3, column=1, sticky=W, columnspan=3)
            apikey_input.grid(row=4, column=1, stick=NSEW, columnspan=3)
            tos_check.grid(row=5, column=1, stick=W)
            tos_label.grid(row=5, column=2, sticky=W, columnspan=2)
            minor_check.grid(row=6, column=1, stick=W)
            minor_label.grid(row=6, column=2, sticky=W, columnspan=2)
            self.user_msg.grid(row=7, column=1, stick=NSEW, columnspan=3)
            self.user_error.grid(row=8, column=1, stick=NSEW, columnspan=3)
            new_usr_submit.grid(row=9, column=1, stick=NSEW, columnspan=3)
            new_usr_back.grid(row=10, column=1, stick=NSEW, columnspan=3)
        else:
            self.main_page()

    # Clear Frame for new page
    def clear_frame(self):
        for widget in self.canvas_body_frame.winfo_children():
            widget.grid_remove()
        self.user_error.config(text="")
        self.user_msg.config(text="")

    # Submit new Error Messages and Checks
    def submit_new(self, usrname_input: str, apikey_input: str, tos: bool, minor: bool):
        error = ""
        if minor is True and tos is True:
            if 0 < len(usrname_input) < 33 and 7 < len(apikey_input) < 129:
                code, response = pixela_commands.new_user(usrname_input, apikey_input)
                if code != 200:
                    error = response.split(".")[0]
                else:
                    self.username = usrname_input
                    self.main_page()
            else:
                if len(usrname_input) == 0 or len(usrname_input) > 33:
                    error = "Username needs to be between\n" \
                             "1 and 32 characters, starting\n" \
                             "with a character, not number."
                elif len(apikey_input) < 7 or len(apikey_input) > 129:
                    error = "API Key needs to be between\n" \
                             "8 and 128 characters."
        else:
            if tos is not True:
                error += "You need to agree to the TOS."
            if minor is not True:
                error += "You need to either not be a minor\n" \
                         "or have parental consent."
        self.user_error.config(text=error.replace('.', '.\n'))

    def new_graph(self):
        self.clear_frame()

        # Labels and Inputs
        graph_id_label = Label(self.canvas_body_frame, text="Graph ID:", fg="white",
                               font=FONT, bg=BACKGROUND_COLOR_2)
        graph_id_input = Entry(self.canvas_body_frame, bg="white")
        graph_id_input.focus()
        graph_name_label = Label(self.canvas_body_frame, text="Graph Name:", fg="white",
                                 font=FONT, bg=BACKGROUND_COLOR_2)
        graph_name_input = Entry(self.canvas_body_frame, bg="white")
        graph_unit_label = Label(self.canvas_body_frame, text="Unit: (i.e. kilogram, calorie, minute)", fg="white",
                                 font=FONT, bg=BACKGROUND_COLOR_2)
        graph_unit_input = Entry(self.canvas_body_frame, bg="white")
        graph_type_label = Label(self.canvas_body_frame, text="Type:", fg="white",
                                 font=FONT, bg=BACKGROUND_COLOR_2)
        type_values = ['Int', 'Float']
        graph_type_input = tkinter.ttk.Combobox(self.canvas_body_frame, font=FONT,
                                                values=type_values, state="readonly")
        graph_type_input.current(0)
        graph_color_label = Label(self.canvas_body_frame, text="Color:", fg="white",
                                  font=FONT, bg=BACKGROUND_COLOR_2)
        color_values = ['Green', 'Red', 'Blue', 'Yellow', 'Purple', 'Black']
        graph_color_input = tkinter.ttk.Combobox(self.canvas_body_frame, font=FONT,
                                                 values=color_values, state="readonly")
        graph_color_input.current(0)
        graph_submit_button = Button(self.canvas_body_frame, text="Submit",
                                     font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                     command=lambda: self.create_graph(
                                         graph_id_input.get().strip(),
                                         graph_name_input.get().strip(),
                                         graph_unit_input.get().strip(),
                                         graph_type_input.get().lower(),
                                         graph_color_input.get().lower()
                                     )
                                     )
        graph_back = Button(self.canvas_body_frame, text="Back", font=FONT,
                            highlightthickness=0, bg=BACKGROUND_COLOR_1, command=self.main_page)

        # Grid Setup
        graph_id_label.grid(row=1, column=1, sticky=W, columnspan=3)
        graph_id_input.grid(row=2, column=1, sticky=NSEW, columnspan=3)
        graph_name_label.grid(row=3, column=1, sticky=W, columnspan=3)
        graph_name_input.grid(row=4, column=1, sticky=NSEW, columnspan=3)
        graph_unit_label.grid(row=5, column=1, sticky=W, columnspan=3)
        graph_unit_input.grid(row=6, column=1, sticky=NSEW, columnspan=3)
        graph_type_label.grid(row=7, column=1, sticky=W)
        graph_type_input.grid(row=7, column=2, sticky=NSEW, columnspan=2)
        graph_color_label.grid(row=8, column=1, sticky=W)
        graph_color_input.grid(row=8, column=2, sticky=NSEW, columnspan=2)
        self.user_msg.grid(row=9, column=1, stick=NSEW, columnspan=3)
        self.user_error.grid(row=10, column=1, stick=NSEW, columnspan=3)
        graph_submit_button.grid(row=11, column=1, sticky=NSEW, columnspan=3)
        graph_back.grid(row=12, column=1, sticky=NSEW, columnspan=3)

    def create_graph(self, graph_id: str, graph_name: str, graph_unit: str, unit_type: str, graph_color: str):
        error = ""
        message = ""
        if not graph_id:
            error += "Please add an ID (1 and 16 characters)."
        if not graph_name:
            error += "Please give the graph a name."
        if not graph_unit:
            error += "Please give the graph a unit type."
        if graph_id and graph_name and graph_unit:
            code, message = pixela_commands.create_graph(self.username, graph_id, graph_name,
                                                         graph_unit, unit_type, graph_color)
            if code == 200:
                self.new_graph()
            elif code == 503:
                error = "Please try again. Support pixela to avoid this."
        if not error:
            self.user_msg.config(text=message)
        else:
            self.user_error.config(text=error.replace('.', '.\n'))

    # Add a datapoint
    def pick_graph(self, button: str):
        # UI Setup
        self.clear_frame()
        graph_select_label = Label(self.canvas_body_frame, text="Select Graph ID:", fg="white",
                                   font=FONT, bg=BACKGROUND_COLOR_2)
        graph_selection = tkinter.ttk.Combobox(self.canvas_body_frame, font=FONT,
                                               values=self.graphs, state="readonly")
        graph_selection.current(0)
        if button == "add":
            graph_submit_button = Button(self.canvas_body_frame, text="Submit",
                                         font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                         command=lambda: self.new_datapoint(graph_selection.get()))
        elif button == "mod":
            graph_submit_button = Button(self.canvas_body_frame, text="Submit",
                                         font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                         command=lambda: self.get_datapoint(graph_selection.get()))
        else:
            graph_submit_button = Button(self.canvas_body_frame, text="ERROR!!",
                                         font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1)
        graph_back = Button(self.canvas_body_frame, text="Back", font=FONT,
                            highlightthickness=0, bg=BACKGROUND_COLOR_1, command=self.main_page)

        # Grid Setup
        graph_select_label.grid(row=1, column=1, sticky=W, columnspan=3)
        graph_selection.grid(row=2, column=1, sticky=NSEW, columnspan=3)
        self.user_msg.grid(row=3, column=1, sticky=NSEW, columnspan=3)
        self.user_error.grid(row=4, column=1, sticky=NSEW, columnspan=3)
        graph_submit_button.grid(row=5, column=1, sticky=NSEW, columnspan=3)
        graph_back.grid(row=6, column=1, sticky=NSEW, columnspan=3)

    def new_datapoint(self, graph_id: str):
        # UI Setup
        self.clear_frame()
        code, resp_unit, name = pixela_commands.get_units(self.username, graph_id)
        if code == 200:
            graph_unit = resp_unit
        else:
            graph_unit = ""
            if code == 503:
                error = "Please try again."
            else:
                error = code
            self.user_error.config(text=error)
        day_select_label = Label(self.canvas_body_frame, text=f"For the graph: {name}",
                                 fg="white", font=FONT, bg=BACKGROUND_COLOR_2)
        day_amt_label = Label(self.canvas_body_frame, text="Amount Today:", fg="white",
                              font=FONT, bg=BACKGROUND_COLOR_2)
        day_amt_input = Entry(self.canvas_body_frame, bg="white")
        day_amt_unit = Label(self.canvas_body_frame, text=f"{graph_unit}", fg="white",
                             font=FONT, bg=BACKGROUND_COLOR_2)
        day_submit_button = Button(self.canvas_body_frame, text="Submit",
                                   font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                   command=lambda: self.submit_new_datapoint(
                                       graph_id,
                                       'today',
                                       day_amt_input.get()
                                   )
                                   )
        day_back = Button(self.canvas_body_frame, text="Back", font=FONT,
                          highlightthickness=0, bg=BACKGROUND_COLOR_1, command=lambda: self.pick_graph("add"))

        # Grid Setup
        day_select_label.grid(row=1, column=1, sticky=W, columnspan=3)
        day_amt_label.grid(row=2, column=1, sticky=W, columnspan=3)
        day_amt_input.grid(row=3, column=1, sticky=NSEW, columnspan=2)
        day_amt_unit.grid(row=3, column=3, sticky=W)
        self.user_msg.grid(row=4, column=1, sticky=NSEW, columnspan=3)
        self.user_error.grid(row=5, column=1, sticky=NSEW, columnspan=3)
        day_submit_button.grid(row=6, column=1, sticky=NSEW, columnspan=3)
        day_back.grid(row=7, column=1, sticky=NSEW, columnspan=3)

    def submit_new_datapoint(self, graph_id: str, day: str, quantity: str):
        code, response = pixela_commands.add_pixel(self.username, graph_id, day, quantity)
        if code == 200:
            self.main_page()
        else:
            if code == 503:
                error = "Please try again,"
            else:
                error = response
            self.user_error.config(text=error)

    def get_datapoint(self, graph_id: str):
        self.clear_frame()
        modified_days = ()
        code, response = pixela_commands.find_datapoints(self.username, graph_id)
        if code == 200:
            days = response
            modified_days = [f'{day[4:6]}/{day[6:]}/{day[0:4]}' for day in reversed(days)]
        else:
            if code == 503:
                error = "Please go back and try again."
            else:
                error = f"Error: {code}"
            self.user_error.config(text=error)

        # UI Setup
        day_select_label = Label(self.canvas_body_frame, text="Select Day:", fg="white",
                                 font=FONT, bg=BACKGROUND_COLOR_2)
        day_selection = tkinter.ttk.Combobox(self.canvas_body_frame, font=FONT,
                                             values=modified_days, state="readonly")
        day_selection.current(0)
        day_submit_button = Button(self.canvas_body_frame, text="Submit",
                                   font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                   command=lambda: self.modify_datapoint(
                                       day_selection.get(),
                                       graph_id
                                   )
                                   )
        day_back = Button(self.canvas_body_frame, text="Back", font=FONT,
                          highlightthickness=0, bg=BACKGROUND_COLOR_1, command=lambda: self.pick_graph("mod"))

        # Grid Setup
        day_select_label.grid(row=1, column=1, sticky=W, columnspan=3)
        day_selection.grid(row=2, column=1, sticky=NSEW, columnspan=3)
        self.user_msg.grid(row=3, column=1, sticky=NSEW, columnspan=3)
        self.user_error.grid(row=4, column=1, sticky=NSEW, columnspan=3)
        day_submit_button.grid(row=5, column=1, sticky=NSEW, columnspan=3)
        day_back.grid(row=6, column=1, sticky=NSEW, columnspan=3)

    def modify_datapoint(self, date: str, graph_id: str):
        self.clear_frame()
        code, response = pixela_commands.get_datapoint_value(self.username, graph_id, date)
        if code == 200:
            current_value = response
        else:
            current_value = ""
            if code == 503:
                error = "Please go back and try again!"
            else:
                error = f"Error: {code}"
            self.user_error.config(text=error)
        code, resp_unit, name = pixela_commands.get_units(self.username, graph_id)
        if code == 200:
            graph_unit = resp_unit
        else:
            graph_unit = ""
            if code == 503:
                error = "Please try again."
            else:
                error = f"Error: {code}"
            self.user_error.config(text=error)

        # UI Setup
        datapoint_label = Label(self.canvas_body_frame, text=f"Value for {date}:", fg="white",
                                font=FONT, bg=BACKGROUND_COLOR_2)
        datapoint_value = Entry(self.canvas_body_frame, bg="white", )
        datapoint_value.focus()
        datapoint_value.insert(END, current_value)
        datapoint_unit = Label(self.canvas_body_frame, text=f'{graph_unit}', fg="white",
                               font=FONT, bg=BACKGROUND_COLOR_2)
        mod_submit_button = Button(self.canvas_body_frame, text="Submit",
                                   font=FONT, highlightthickness=0, bg=BACKGROUND_COLOR_1,
                                   command=lambda: self.submit_new_datapoint(
                                       graph_id,
                                       date,
                                       datapoint_value.get()
                                   )
                                   )
        mod_back = Button(self.canvas_body_frame, text="Back", font=FONT,
                          highlightthickness=0, bg=BACKGROUND_COLOR_1, command=lambda: self.get_datapoint(graph_id))

        # Grid Setup
        datapoint_label.grid(row=1, column=1, sticky=W, columnspan=3)
        datapoint_value.grid(row=2, column=1, sticky=NSEW, columnspan=2)
        datapoint_unit.grid(row=2, column=3, sticky=W)
        self.user_msg.grid(row=3, column=1, sticky=NSEW, columnspan=3)
        self.user_error.grid(row=4, column=1, sticky=NSEW, columnspan=3)
        mod_submit_button.grid(row=5, column=1, sticky=NSEW, columnspan=3)
        mod_back.grid(row=6, column=1, sticky=NSEW, columnspan=3)

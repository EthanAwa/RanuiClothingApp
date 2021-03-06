from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

class Gui:

    def __init__(self, parent):
        # Main Background color, others will be specified when used
        background = "#C402DE" # Dark pink, contrasts with other colors in the 3 color filters on Windows.

        # Set up styling for tkk.[object], which usually can't have styling such as bg="", fg="", etc.
        style = Style()
        style.configure("TButton", font=("Arial", 11), bd=3) # ttk.Button doesn't allow for "font='' " unless in Style()

        # Child name (printing for testing)
        self.name = StringVar()

        # Base allowance of 300
        self.allowance = 300

        # Frame to contain everything
        self.main_frame = Frame(bg=background, pady=10)
        self.main_frame.grid(columnspan=3)

        # Main window title, row 0
        self.title_label = Label(bg=background, text="Ranui Family Allowance Tracker",
                                 font=("Arial", 20, "bold"), fg="white", justify=CENTER)
        self.title_label.grid(row=0, columnspan=3)

        # 3 radio buttons, 1 for each child. Row 1
        # The color #C47FDE is a light purple, contrasts with the background color in all Windows color filters.
        self.nikau_button = Radiobutton(text="Nikau", variable=self.name, value="Nikau",
                                        command=self.print, indicator=0, font=("Arial", 15, "bold"),
                                        background="#C47FDE", fg="black")
        self.hana_button = Radiobutton(text="Hana", variable=self.name, value="Hana",
                                       command=self.print, indicator=0, font=("Arial", 15, "bold"),
                                       background="#C47FDE", fg="black")
        self.tia_button = Radiobutton(text="Tia", variable=self.name, value="Tia",
                                      command=self.print, indicator=0, font=("Arial", 15, "bold"),
                                      background="#C47FDE", fg="black")
        self.nikau_button.grid(row=1, column=0)
        self.hana_button.grid(row=1, column=1)
        self.tia_button.grid(row=1, column=2)

        # User enters how much clothing costs, row 2
        self.allowance_label = Label(bg=background, text="Cost of clothing", justify=RIGHT, font="Helvetica 14", fg="white")
        self.allowance_entry = Entry(bd=2, font=("Helvetica", 12), relief=SUNKEN)
        self.allowance_button = ttk.Button(text="Buy Clothing")
        self.allowance_label.grid(row=2, column=0)
        self.allowance_entry.grid(row=2, column=1)
        self.allowance_button.grid(row=2, column=2, padx=5)

        # Show the child's allowance, row 3
        self.show_allowance = Label(bg=background, text="Pick a kid to see their allowance.",
                                    font=("Helvetica", 14, "bold"), fg="white")
        self.show_allowance.grid(row=3, columnspan=3)

        # Button to check/change bonuses, row 4.
        self.bonus_check_btn = ttk.Button(text="Bonuses", command=print("Who can get the bonus"))
        self.bonus_check_btn.grid(row=4, column=0)

        # Button to signify end of year. Will be used to check for bonus once user wants to, row 4.
        self.end_year_btn = ttk.Button(text="End the year", command=print("Year has ended."))
        self.end_year_btn.grid(row=4, column=1)

        # Help button, instructions + possible video, row 4
        self.help_btn = ttk.Button(text="Instructions", command=print("Help me!"))
        self.help_btn.grid(row=4, column=2)

    # Prints out whatever kid you pick in show_allowance text field. Just to see if button selection works.
    def print(self):
        text = f"{self.name.get()}\'s Allowance: {self.allowance}"
        self.show_allowance.configure(text=text)

if __name__ == '__main__':
    root = Tk()
    root.title("Ranui Clothing App")
    root.configure(background="#C402DE")
    window = Gui(root)
    root.mainloop()

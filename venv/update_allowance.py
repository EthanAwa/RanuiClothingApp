from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

class Ranui:
    def __init__(self, name, allowance):
        self.name = name
        self.allowance = allowance

nikau = Ranui("Nikau", 300)
hana = Ranui("Hana", 300)
tia = Ranui("Tia", 300)

# test = nikau
# print(test.name, test.allowance)

class Gui:

    def __init__(self, parent):
        # Main Background color, others will be specified when used
        background = "#C402DE" # Dark pink, contrasts with other colors in the 3 color filters on Windows.

        # Set up styling for tkk.[object], which usually can't have styling such as bg="", fg="", etc.
        style = Style()
        style.configure("TButton", font=("Arial", 11), bd=3) # ttk.Button doesn't allow for "font='' " unless in Style()

        # Child name (printing for testing)
        self.name = StringVar()

        # # Base allowance of 300
        # self.allowance = 300

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
        self.allowance_button = ttk.Button(text="Buy Clothing", command = self.buy_item)
        self.allowance_label.grid(row=2, column=0)
        self.allowance_entry.grid(row=2, column=1)
        self.allowance_button.grid(row=2, column=2, padx=5)

        # Show the child's allowance, row 3
        self.show_allowance = Label(bg=background, text="Pick a kid to see their allowance.",
                                    font=("Helvetica", 14, "bold"), fg="white")
        self.show_allowance.grid(row=3, columnspan=3)

    # Print command
    def print(self):
        name = self.name.get()
        if name == "Nikau":
            name = nikau
        elif name == "Hana":
            name = hana
        else:
            name = tia

        text = f"{name.name}\'s Allowance: ${name.allowance}"
        self.show_allowance.configure(text=text)

    # Is input integer? (Currently only used in buy_item, may be used in other places though)
    def isint(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    # Function to remove clothing cost from allowance
    def buy_item(self):
        name = self.name.get()
        cost = self.allowance_entry.get()

        # Check what kid is selected
        if name == "Nikau":
            name = nikau
        elif name == "Hana":
            name = hana
        elif name == "Tia":
            name = tia

        # Calls isint(), basic input checker
        cost_check = self.isint(cost)

        # If no kid has been selected...
        if name not in [nikau, hana, tia]:
            text = "Please choose one of the kids."
            self.show_allowance.configure(text=text)

        # If a kid is selected, but the entry box is blank...
        elif cost == '':
            text = "Please enter a whole number larger than 0."
            self.show_allowance.configure(text=text)

        # If the input is a string or float...
        elif cost_check == False:
            text = "Please enter a whole number larger than 0."
            self.show_allowance.configure(text=text)

        # If the input is an integer...
        else:
            name.allowance = name.allowance - int(cost)
            print(name.allowance)
            text = f"{name.name}\'s Allowance: ${name.allowance}"
            self.show_allowance.configure(text=text)
            print("hopefully only shows when successful")


if __name__ == '__main__':
    root = Tk()
    root.title("Ranui Clothing App")
    root.configure(background="#C402DE")
    window = Gui(root)
    root.mainloop()
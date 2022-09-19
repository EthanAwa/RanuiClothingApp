import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Style

class Ranui:
    def __init__(self, name, allowance, bonus, check): # Check = is child eligible for the bonus.
        self.name = name
        self.allowance = allowance
        self.bonus = bonus
        self.check = check

nikau = Ranui("Nikau", 300, "", True)
hana = Ranui("Hana", 300, "", True)
tia = Ranui("Tia", 300, "", True)

class Gui():

    def __init__(self, parent):
        # Main Background color, others will be specified when used
        background = "#C402DE" # Dark purple, contrasts with other colors in the 3 color filters on Windows.

        # Set up styling for tkk.[object], which usually can't have styling such as bg="", fg="", etc.
        style = Style()
        style.configure("TButton", font=("Arial", 11), bd=3) # ttk.Button doesn't allow for "font='' " unless in Style()

        self.name = StringVar()
        #
        # # Base allowance of 300
        # self.allowance = 300

        # Frame to contain everything
        self.main_frame = Frame(bg=background, pady=10, padx=3)
        self.main_frame.grid(columnspan=3)

        # Main window title, row 0
        self.title_label = Label(bg=background, text="Ranui Family Allowance Tracker",
                                 font=("Arial", 20, "bold"), fg="white", justify=CENTER)
        self.title_label.grid(row=0, columnspan=3, pady=3)

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
        self.allowance_label = Label(bg=background, text="Cost of clothing", justify=RIGHT,
                                     font="Arial 13 bold", fg="white")
        self.allowance_entry = Entry(bd=2, font=("Arial", 12), relief=SUNKEN)
        self.allowance_button = ttk.Button(text="Buy Clothing", command = self.buy_item)
        self.allowance_label.grid(row=2, column=0, padx=10, pady=5)
        self.allowance_entry.grid(row=2, column=1, padx=10, pady=5)
        self.allowance_button.grid(row=2, column=2, padx=10, pady=5)

        # Show the child's allowance, row 3
        self.show_allowance = Label(bg=background, text="Pick a kid to see their allowance.",
                                    font=("Arial", 14, "bold"), fg="white")
        self.show_allowance.grid(row=3, columnspan=3, padx=10, pady=5)

        # Button to check/change bonuses, row 4.
        self.bonus_check_btn = ttk.Button(text="Bonuses", command=self.bonus)
        self.bonus_check_btn.grid(row=4, column=0, padx=5, pady=10)

        # Button to signify end of year. Will be used to check for bonus once user wants to, row 4.
        self.end_year_btn = ttk.Button(text="End the year", command=lambda: self.end_year(self.disable))
        self.end_year_btn.grid(row=4, column=1, padx=5, pady=10)

        # Help button, instructions + possible video, row 4
        self.help_btn = ttk.Button(text="Instructions", command=self.instructions)
        self.help_btn.grid(row=4, column=2, padx=5, pady=10)
        self.askuser()

        # List of all buttons/entry boxes to be disabled later
        self.disable = [self.nikau_button, self.hana_button, self.tia_button, self.allowance_button,
                   self.allowance_entry, self.help_btn, self.bonus_check_btn, self.end_year_btn]

    # Asks the user if they've used the program before
    def askuser(self):
        res = messagebox.askquestion("Dear User", "Have you used this program before?")
        if res == "no":
            messagebox.showinfo("Instructions",
                                "Step 1: Pick the kid whose allowance you are spending.\n"
                                "Step 2: Enter the cost of the clothing into the box under the names.\n"
                                "Step 3: Press the \"Buy Clothing\" button to buy the clothing.\n\n"
                                "More information about other parts of the program can be found by pressing the "
                                "\"Instructions\" button.")
        else:
            messagebox.showinfo("Enjoy", "Cool, enjoy using the program.")

    def instructions(self):
        messagebox.showinfo("Instructions: How to Buy Clothing",
                            "In this Allowance Tracker, you are able to select the child who is "
                            "spending money. To do so, click on their name at the top of the program, "
                            "and type in the amount they are spending in the box below. Then, press "
                            "the \"Buy Clothing\" button to take that money out of their allowance.")

        messagebox.showinfo("Instructions: Bonuses",
                            "If at any point one of the kids allowances goes below $50, they will "
                            "no longer be able to get the bonus of their choice.")

        messagebox.showinfo("Instructions: Ending the Year",
                            "If you would like the end the year, you can press the button at the middle bottom "
                            "of the screen. This button will stop you from being able to input anything in "
                            "the main window, and will bring up an overview of each kid's allowance, their bonus, "
                            "and if they can get it or not.")


    # Prints out whatever kid you pick in show_allowance text field. Just to see if button selection works.
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
    def is_int(self, num):
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

        # Calls is_int(), basic input checker
        cost_check = self.is_int(cost)

        # If no kid has been selected...
        if name not in [nikau, hana, tia]:
            text = "Please choose one of the kids."

        # If a kid is selected, but the entry box is blank or is 0...
        elif cost == '' or int(cost) == 0:
            text = "Please enter a whole number larger than 0."

        # If the input is a string or float...
        elif cost_check == False:
            text = "Please enter a whole number larger than 0."

        # If the input is over current allowance or negative...
        elif int(cost) < 0 or name.allowance - int(cost) < 0:
            text = "You can't add money or overspend your allowance."

        # If the input is an integer...
        else:
            name.allowance = name.allowance - int(cost)
            text = f"{name.name}\'s Allowance: ${name.allowance}"
        self.show_allowance.configure(text=text)

    # End the Year Button window
    def end_year(self, children):
        if nikau.bonus == "" or hana.bonus == "" or tia.bonus == "":
            messagebox.showwarning("Bonuses Not Assigned",
                                   "Please let your children pick a bonus using the \"Bonuses\" button.")
        else:
            res = messagebox.askquestion("Warning",
                                         "Are you sure that you want to end the year? Ending the year will "
                                         "disable all input in the Allowance Manager.")
            if res == "yes":
                for widget in children:
                    widget.configure(state=DISABLED)
                End_Year(self)
            else:
                messagebox.showinfo("Warning", "Enjoy using the program again.")

    def bonus(self):
        Bonus()

class End_Year:

    # Disable Windows built in [X] button
    def disable_exit(self):
        pass

    def __init__(self, partner):
        background = "#D94F2B"

        # Spawn new window above main window
        self.overview_box = Toplevel()

        # Disable Windows built in [X] button
        self.overview_box.protocol("WM_DELETE_WINDOW", self.disable_exit)

        # Set up overview window frame
        self.overview_frame = Frame(self.overview_box, bg=background, pady=10, padx=3)
        self.overview_frame.grid()

        # Title label
        self.title = Label(self.overview_frame, text="Overview of the Year",
                           font="Arial 20 bold", bg=background, fg="white")
        self.title.grid(columnspan=2, row=0)

        # # Following comments/code sections will be removed in final product, only exist for testing here.
        # # For now, show a message saying "The year has ended, thank for you using the program."
        # self.test_msg = Label(self.overview_frame, text="The year has been ended.\nThank you for using the program.",
        #                       font="Arial 15", bg=background, fg="white")
        # self.test_msg.grid(columnspan=2, row=1)

        self.overview = Label(self.overview_frame, text="Here's how your children's spending looks.",
                              font="Arial 16 bold", bg=background, fg="white")
        self.overview.grid(columnspan=2, row=1)

        # Loop to add children spending/bonus into overview window, more effecient.
        # Row counter
        k = 2
        for i in range(3):
            name = [nikau, hana, tia]
            if name[i].allowance < 50:
                name[i].check = False
            check = name[i].check

            # Bonus check
            if check == True:
                check = f"{name[i].name} can get their bonus ({name[i].bonus})."
            else:
                check = f"{name[i].name} can not get their bonus ({name[i].bonus})"

            # Name/allowance Label
            self.kid_overview = Label(self.overview_frame, text=f"{name[i].name}: ${name[i].allowance}",
                                      font="Arial 14", bg=background, fg="white")
            # Bonus check Label
            self.kid_overview_bonus = Label(self.overview_frame, text=f"{check}",
                                            font="Arial 14", bg=background, fg="white")
            self.kid_overview.grid(column=0, row=k)
            self.kid_overview_bonus.grid(column=1, row=k)
            print(name[i].name, name[i].allowance, name[i].bonus, name[i].check)
            k += 1

        # Tell user to press close to shut down program
        self.close_label = Label(self.overview_frame, text="Press the Close button to close the program.",
                                 font="Arial 15 bold", bg=background, fg="white")
        self.close_btn = Button(self.overview_frame, text="Close", font="Arial 13 bold",
                                bg="#F07A3B", fg="white", command=self.close)
        self.close_label.grid(columnspan=2, row=5)
        self.close_btn.grid(columnspan=2, row=6)

    def close(self):
        messagebox.showinfo("Thank You",
                            "Thank you for using this program.")
        root.destroy()

class Bonus:

    # Disable Windows built in [X] button
    def disable_exit(self):
        pass

    def __init__(self):
        background = "#3E76ED"

        self.name = StringVar()

        # Spawn new window above main window
        self.bonus_box = Toplevel()

        # Disable Windows built in [X] button
        self.bonus_box.protocol("WM_DELETE_WINDOW", self.disable_exit)

        # Set up bonus window frame
        self.bonus_frame = Frame(self.bonus_box, bg=background, pady=10, padx=3)
        self.bonus_frame.grid()

        # Window Header
        self.bonus_header = Label(self.bonus_frame, text="Pick your children's bonuses",
                                  font="Arial 16 bold", bg=background, fg="white")
        self.bonus_header.grid(row=0, columnspan=3)

        # RadioButton for child selection
        self.nikau_button = Radiobutton(self.bonus_frame, text="Nikau", variable=self.name, value="Nikau",
                                        command=self.print, indicator=0, font=("Arial", 15, "bold"),
                                        background="#34D8F7", fg="black")
        self.hana_button = Radiobutton(self.bonus_frame, text="Hana", variable=self.name, value="Hana",
                                       command=self.print, indicator=0, font=("Arial", 15, "bold"),
                                       background="#34D8F7", fg="black")
        self.tia_button = Radiobutton(self.bonus_frame, text="Tia", variable=self.name, value="Tia",
                                      command=self.print, indicator=0, font=("Arial", 15, "bold"),
                                      background="#34D8F7", fg="black")
        self.nikau_button.grid(row=1, column=0)
        self.hana_button.grid(row=1, column=1)
        self.tia_button.grid(row=1, column=2)

        # Entry box section
        self.bonus_label = Label(self.bonus_frame, bg=background, text="Child's Bonus", justify=RIGHT,
                                 font="Arial 13 bold", fg="white")
        self.bonus_entry = Entry(self.bonus_frame, bd=2, font=("Arial", 12), relief=SUNKEN)
        self.bonus_button = ttk.Button(self.bonus_frame, text="Set Bonus", command=self.setbonus)
        self.bonus_label.grid(row=2, column=0, padx=10, pady=5)
        self.bonus_entry.grid(row=2, column=1, padx=10, pady=5)
        self.bonus_button.grid(row=2, column=2, padx=10, pady=5)

        # Show who has been selected
        self.show_bonus = Label(self.bonus_frame, bg=background, text="Pick a kid to see their bonus.",
                                font=("Arial", 14, "bold"), fg="white")
        self.show_bonus.grid(row=3, columnspan=3, padx=10, pady=5)

        # Tell user to hit close to close this window
        self.close_label = Label(self.bonus_frame, text="Press the Close button to close this window",
                                 font="Arial 15 bold", bg=background, fg="white")
        self.close_label.grid(row=4, columnspan=3)
        # Close Button
        self.close = Button(self.bonus_frame, text="Close", font="Arial 13 bold",
                            bg="#34D8F7", fg="black", command=self.bonus_box.destroy)
        self.close.grid(row=5, columnspan=3)

    # Update show_bonus with the child selected
    def print(self):
        name = self.name.get()
        if name == "Nikau":
            name = nikau
        elif name == "Hana":
            name = hana
        else:
            name = tia

        text = f"{name.name}\'s bonus: {name.bonus}"
        self.show_bonus.configure(text=text)

    def setbonus(self):
        name = self.name.get()
        bonus = self.bonus_entry.get()

        # Check what kid is selected
        if name == "Nikau":
            name = nikau
        elif name == "Hana":
            name = hana
        elif name == "Tia":
            name = tia

        # If no kid has been selected...
        if name not in [nikau, hana, tia]:
            text = "Please choose one of the kids."
        elif bonus == "" or bonus == " ":
            text = "Please enter a bonus, this can not be blank."
        else:
            name.bonus = bonus
            text = f"{name.name}'s bonus: {name.bonus}"
        self.show_bonus.configure(text=text)

if __name__ == '__main__':
    root = Tk()
    root.title("Ranui Clothing App")
    root.configure(background="#C402DE")
    root.resizable(False, False)
    window = Gui(root)
    root.mainloop()

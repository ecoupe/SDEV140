from breezypythongui import EasyFrame
from tkinter import messagebox, IntVar
from tkinter.ttk import Combobox, Radiobutton
import random

class PasswordManagerGenerator(EasyFrame):
    def __init__(self):
        # Initialize the main window
        EasyFrame.__init__(self, title="Soapbox Password Manager & Generator", width=600, height=350)
        
        # Password Generation Section
        self.addLabel(text="PASSWORD GENERATOR", row=0, column=0, columnspan=4, sticky="w")
        
        # Password Display
        self.addLabel(text="Generated Password:", row=1, column=0)
        self.entryGenerated = self.addTextField(text="", row=1, column=1, columnspan=2, sticky="we")
        
        # Password Length
        self.addLabel(text="Length:", row=2, column=0)
        self.var1 = IntVar()
        self.comboLength = Combobox(self, textvariable=self.var1, width=10)
        self.comboLength['values'] = tuple(range(8, 33)) + ("Length",)
        self.comboLength.current(0)
        self.comboLength.grid(row=2, column=1, sticky="w")
        
        # Password Strength
        self.addLabel(text="Strength:", row=3, column=0)
        self.var = IntVar(value=0)  # Default to Medium
        self.radioLow = Radiobutton(self, text="Low", variable=self.var, value=1)
        self.radioLow.grid(row=3, column=1, sticky="w")
        self.radioMedium = Radiobutton(self, text="Medium", variable=self.var, value=0)
        self.radioMedium.grid(row=3, column=2, sticky="w")
        self.radioStrong = Radiobutton(self, text="Strong", variable=self.var, value=3)
        self.radioStrong.grid(row=3, column=3, sticky="w")
        
        # Generate Button
        self.addButton(text="Generate", row=4, column=0, columnspan=4, command=self.generate_password)
        
        # Password Manager Section
        self.addLabel(text="PASSWORD MANAGER", row=5, column=0, columnspan=4, sticky="w")
        
        # Username
        self.addLabel(text="USERNAME:", row=6, column=0, sticky="w")
        self.entryName = self.addTextField(text="", row=6, column=1, columnspan=3, sticky="we")
        
        # Password
        self.addLabel(text="PASSWORD:", row=7, column=0, sticky="w")
        self.entryPassword = self.addTextField(text="", row=7, column=1, columnspan=3, sticky="we")

        # Action Buttons
        self.addButton(text="Add", row=8, column=0, command=self.add_info)
        self.addButton(text="Get", row=8, column=1, command=self.retrieve_info)
        self.addButton(text="List", row=8, column=2, command=self.getlist)
        self.addButton(text="Delete", row=8, column=3, command=self.delete)

    def generate_password(self):
        # Get length and strength
        length = int(self.comboLength.get()) if self.comboLength.get() != "Length" else 12
        strength = self.var.get()
        
        # Define character sets
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
        
        # Generate password based on strength
        password = ""
        if strength == 1:  # Low
            password = ''.join(random.choice(lower) for _ in range(length))
        elif strength == 0:  # Medium
            password = ''.join(random.choice(upper) for _ in range(length))
        elif strength == 3:  # Strong
            password = ''.join(random.choice(digits) for _ in range(length))
        else:
            messagebox.showerror("Error", "Please choose a strength option")
            return
        
        # Display generated password
        self.entryGenerated.setText(password)
        # Optionally, also set this as the password to add
        self.entryPassword.setText(password)

    def add_info(self):
        username = self.entryName.getText()
        password = self.entryPassword.getText()

        if username and password:
            with open("soapboxes_galore.txt", 'a') as f:
                f.write(f"{username} {password}\n")
            messagebox.showinfo("Success", "Password added!")
        else:
            messagebox.showerror("Error", "Please enter both a Username AND a Password")

    def retrieve_info(self):
        username = self.entryName.getText()
        passwords = {}

        try:
            with open("soapboxes_galore.txt", 'r') as f:
                for k in f:
                    i = k.strip().split(' ')
                    passwords[i[0]] = i[1]
        except FileNotFoundError:
            messagebox.showerror("Error", "No password file found!")
            return

        if passwords:
            message = "Your passwords:\n"
            for i in passwords:
                if i == username:
                    message += f"Password for {username} is {passwords[i]}\n"
                    break
            else:
                message = "No such Username Exists"
            messagebox.showinfo("Passwords", message)
        else:
            messagebox.showinfo("Passwords", "Empty List!")

    def getlist(self):
        passwords = {}

        try:
            with open("soapboxes_galore.txt", 'r') as f:
                for k in f:
                    i = k.strip().split(' ')
                    passwords[i[0]] = i[1]
        except FileNotFoundError:
            messagebox.showerror("Error", "No password file found!")
            return

        if passwords:
            mess = "List of passwords:\n"
            for name, password in passwords.items():
                mess += f"Password for {name} is {password}\n"
            messagebox.showinfo("Passwords", mess)
        else:
            messagebox.showinfo("Passwords", "Empty List!")

    def delete(self):
        username = self.entryName.getText()
        temp_passwords = []

        try:
            with open("soapboxes_galore.txt", 'r') as f:
                for k in f:
                    i = k.strip().split(' ')
                    if i[0] != username:
                        temp_passwords.append(f"{i[0]} {i[1]}")

            with open("soapboxes_galore.txt", 'w') as f:
                for line in temp_passwords:
                    f.write(line + '\n')

            messagebox.showinfo("Success", f"User {username} deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting user {username}: {e}")

if __name__ == "__main__":
    PasswordManagerGenerator().mainloop()



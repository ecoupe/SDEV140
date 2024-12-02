from breezypythongui import EasyFrame
from tkinter import messagebox

class PasswordManager(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Soapbox Password Manager", width=560, height=270)
        
        # Username
        self.addLabel(text="USERNAME:", row=0, column=0, sticky="w")
        self.entryName = self.addTextField(text="", row=0, column=1, sticky="we")
        
        # Password
        self.addLabel(text="PASSWORD:", row=1, column=0, sticky="w")
        self.entryPassword = self.addTextField(text="", row=1, column=1, sticky="we")

        # Add button
        self.addButton(text="Add", row=2, column=0, columnspan=2, command=self.add_info).grid(sticky="w")

        # Get button
        self.addButton(text="Get", row=3, column=0, columnspan=2, command=self.retrieve_info).grid(sticky="w")

        # List Button
        self.addButton(text="List", row=4, column=0, columnspan=2, command=self.getlist).grid(sticky="w")

        # Delete button
        self.addButton(text="Delete", row=5, column=0, columnspan=2, command=self.delete).grid(sticky="w")

        

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
                    i = k.split(' ')
                    passwords[i[0]] = i[1]
        except:
            print("Error!")

        if passwords:
            message = "Your passwords:\n"
            for i in passwords:
                if i == username:
                    message += f"Password for {username} is {passwords[i]}\n"
                    break
            else:
                message += "No such Username Exists"
            messagebox.showinfo("Passwords", message)
        else:
            messagebox.showinfo("Passwords", "Empty List!")

    def getlist(self):
        passwords = {}

        try:
            with open("soapboxes_galore.txt", 'r') as f:
                for k in f:
                    i = k.split(' ')
                    passwords[i[0]] = i[1]
        except:
            print("No passwords found!!")

        if passwords:
            mess = "List of passwords:\n"
            for name, password in passwords.items():
                mess += f"Password for {name} is {password}\n"
            messagebox.showinfo("Passwords", mess)
        else:
            messagebox.showinfo("Passwords", "Empty List !!")

    def delete(self):
        username = self.entryName.getText()
        temp_passwords = []

        try:
            with open("soapboxes_galore.txt", 'r') as f:
                for k in f:
                    i = k.split(' ')
                    if i[0] != username:
                        temp_passwords.append(f"{i[0]} {i[1]}")

            with open("soapboxes_galore.txt", 'w') as f:
                for line in temp_passwords:
                    f.write(line)

            messagebox.showinfo("Success", f"User {username} deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting user {username}: {e}")

if __name__ == "__main__":
    PasswordManager().mainloop()

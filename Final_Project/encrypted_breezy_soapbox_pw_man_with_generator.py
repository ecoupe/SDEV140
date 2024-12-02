from breezypythongui import EasyFrame
from tkinter import messagebox, IntVar, simpledialog
from tkinter.ttk import Combobox, Radiobutton
import random
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordManagerGenerator(EasyFrame):
    def __init__(self):
        # Master password file
        self.MASTER_PASSWORD_FILE = "master.key"
        self.ENCRYPTED_FILE = "soapboxes_galore.enc"
        
        # Initialize the main window
        EasyFrame.__init__(self, title="Soapbox Password Manager & Generator", width=600, height=400)
        
        # First, check for master password
        if not self.check_master_password():
            self.destroy()
            return
        
        # Load encryption key
        self.encryption_key = self.load_or_create_key()
        
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

    def check_master_password(self):
        """Check or create master password for the application."""
        # If master password file doesn't exist, create it
        if not os.path.exists(self.MASTER_PASSWORD_FILE):
            # First-time setup
            master_password = simpledialog.askstring(
                "First Time Setup", 
                "Create a Master Password:\n(This will be used to access the Password Manager)", 
                show='*'
            )
            
            if not master_password:
                messagebox.showerror("Error", "Master password is required!")
                return False
            
            # Verify password
            confirm_password = simpledialog.askstring(
                "Confirm Password", 
                "Confirm Master Password:", 
                show='*'
            )
            
            if master_password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match!")
                return False
            
            # Hash and store the master password
            self.hash_and_store_master_password(master_password)
            return True
        
        # Existing app - ask for master password
        attempts = 3
        while attempts > 0:
            entered_password = simpledialog.askstring(
                "Login", 
                f"Enter Master Password (Attempts left: {attempts}):", 
                show='*'
            )
            
            if self.verify_master_password(entered_password):
                return True
            
            attempts -= 1
            
        messagebox.showerror("Error", "Too many incorrect attempts. Exiting.")
        return False

    def hash_and_store_master_password(self, password):
        """Securely hash and store the master password."""
        # Use SHA-256 for hashing
        digest = hashes.Hash(hashes.SHA256())
        digest.update(password.encode())
        hashed_password = digest.finalize()
        
        # Store hashed password
        with open(self.MASTER_PASSWORD_FILE, 'wb') as f:
            f.write(hashed_password)

    def verify_master_password(self, entered_password):
        """Verify the entered master password."""
        # Hash the entered password
        digest = hashes.Hash(hashes.SHA256())
        digest.update(entered_password.encode())
        hashed_entered = digest.finalize()
        
        # Read stored hash
        with open(self.MASTER_PASSWORD_FILE, 'rb') as f:
            stored_hash = f.read()
        
        # Compare hashes
        return hashed_entered == stored_hash

    def load_or_create_key(self):
        """Generate or load an encryption key."""
        # Salt for key derivation
        salt = b'soapbox_password_manager_salt'
        
        # Derive key from master password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        
        # Read master password to derive key
        with open(self.MASTER_PASSWORD_FILE, 'rb') as f:
            master_hash = f.read()
        
        # Derive encryption key
        key = base64.urlsafe_b64encode(kdf.derive(master_hash))
        return Fernet(key)

    def encrypt_passwords(self, passwords):
        """Encrypt passwords before storing."""
        encrypted_data = self.encryption_key.encrypt(passwords.encode())
        with open(self.ENCRYPTED_FILE, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_passwords(self):
        """Decrypt passwords from file."""
        try:
            with open(self.ENCRYPTED_FILE, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_data = self.encryption_key.decrypt(encrypted_data).decode()
            return decrypted_data
        except FileNotFoundError:
            return ""
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))
            return ""

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

        if not username or not password:
            messagebox.showerror("Error", "Please enter both a Username AND a Password")
            return

        # Retrieve existing passwords
        existing_passwords = self.decrypt_passwords()
        
        # Add new password
        if existing_passwords:
            existing_passwords += f"\n{username} {password}"
        else:
            existing_passwords = f"{username} {password}"
        
        # Encrypt and save
        self.encrypt_passwords(existing_passwords)
        messagebox.showinfo("Success", "Password added!")

    def retrieve_info(self):
        username = self.entryName.getText()
        
        # Decrypt passwords
        passwords_str = self.decrypt_passwords()
        
        if not passwords_str:
            messagebox.showinfo("Passwords", "Empty List!")
            return

        # Parse passwords
        passwords = {}
        for line in passwords_str.split('\n'):
            parts = line.split(' ', 1)
            if len(parts) == 2:
                passwords[parts[0]] = parts[1]

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
        # Decrypt passwords
        passwords_str = self.decrypt_passwords()
        
        if not passwords_str:
            messagebox.showinfo("Passwords", "Empty List!")
            return

        # Parse passwords
        passwords = {}
        for line in passwords_str.split('\n'):
            parts = line.split(' ', 1)
            if len(parts) == 2:
                passwords[parts[0]] = parts[1]

        if passwords:
            mess = "List of passwords:\n"
            for name, password in passwords.items():
                mess += f"Password for {name} is {password}\n"
            messagebox.showinfo("Passwords", mess)
        else:
            messagebox.showinfo("Passwords", "Empty List!")

    def delete(self):
        username = self.entryName.getText()
        
        # Decrypt passwords
        passwords_str = self.decrypt_passwords()
        
        if not passwords_str:
            messagebox.showinfo("Passwords", "Empty List!")
            return

        # Parse and filter out the username to delete
        temp_passwords = []
        for line in passwords_str.split('\n'):
            parts = line.split(' ', 1)
            if len(parts) == 2 and parts[0] != username:
                temp_passwords.append(line)

        # Rejoin and encrypt
        new_passwords_str = '\n'.join(temp_passwords)
        self.encrypt_passwords(new_passwords_str)

        messagebox.showinfo("Success", f"User {username} deleted successfully!")

if __name__ == "__main__":
    PasswordManagerGenerator().mainloop()
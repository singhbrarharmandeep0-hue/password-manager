import customtkinter as ctk
from database import create_database

# Create database
create_database()

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Main application
app = ctk.CTk()

app.title("Password Manager")
app.geometry("900x600")


# -----------------------------
# Functions
# -----------------------------

def add_password():
    print("Add password clicked")


def view_passwords():
    print("View passwords clicked")


# -----------------------------
# Dashboard
# -----------------------------

title = ctk.CTkLabel(
    app,
    text="🔐 Password Manager",
    font=("Arial", 30, "bold")
)

title.pack(pady=(40, 10))


subtitle = ctk.CTkLabel(
    app,
    text="Manage your passwords securely",
    font=("Arial", 16)
)

subtitle.pack(pady=(0, 40))


# Add password button

add_button = ctk.CTkButton(
    app,
    text="+ Add Password",
    width=250,
    height=50,
    font=("Arial", 16),
    command=add_password
)

add_button.pack(pady=15)


# View passwords button

view_button = ctk.CTkButton(
    app,
    text="👁 View Passwords",
    width=250,
    height=50,
    font=("Arial", 16),
    command=view_passwords
)

view_button.pack(pady=15)


# Run application

app.mainloop()

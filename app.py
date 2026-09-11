import customtkinter as ctk

from database import create_database, add_password, get_passwords

from encryption import encrypt_password, decrypt_password

create_database()
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

def open_add_password():

    add_window = ctk.CTkToplevel(app)

    add_window.title("Add Password")
    add_window.geometry("500x500")

    title = ctk.CTkLabel(
        add_window,
        text="Add New Password",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=30)

    account_entry = ctk.CTkEntry(
        add_window,
        placeholder_text="Account name",
        width=350,
        height=45
    )

    account_entry.pack(pady=10)

    username_entry = ctk.CTkEntry(
        add_window,
        placeholder_text="Username / Email",
        width=350,
        height=45
    )

    username_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(
        add_window,
        placeholder_text="Password",
        show="*",
        width=350,
        height=45
    )

    password_entry.pack(pady=10)


    def save():

        account = account_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        if not account or not username or not password:
            print("Please fill all fields")
            return

        add_password(account, username, password)

        print("Password saved successfully!")

        add_window.destroy()


    save_button = ctk.CTkButton(
        add_window,
        text="Save Password",
        width=200,
        height=45,
        command=save
    )

    save_button.pack(pady=30)


def view_passwords():
    print("View passwords clicked")

    passwords = get_passwords()
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
    command=open_add_password
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

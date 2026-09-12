import customtkinter as ctk

from database import (
    create_database,
    add_password,
    get_passwords
)

from encryption import (
    encrypt_password,
    decrypt_password
)


# -----------------------------
# Database
# -----------------------------

create_database()


# -----------------------------
# Appearance
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# -----------------------------
# Main window
# -----------------------------

app = ctk.CTk()

app.title("Password Manager")

app.geometry("900x600")


# -----------------------------
# Master password
# -----------------------------

master_password = ""


# -----------------------------
# Login function
# -----------------------------

def unlock():

    global master_password

    password = master_entry.get()

    if not password:

        status_label.configure(
            text="Please enter your master password."
        )

        return

    master_password = password

    login_frame.pack_forget()

    dashboard_frame.pack(
        fill="both",
        expand=True
    )


# -----------------------------
# Add password window
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

            status.configure(
                text="Please fill all fields."
            )

            return


        encrypted_password = encrypt_password(
            master_password,
            password
        )


        add_password(
            account,
            username,
            encrypted_password
        )


        status.configure(
            text="Password saved successfully!"
        )


        add_window.destroy()


    save_button = ctk.CTkButton(
        add_window,
        text="Save Password",
        width=200,
        height=45,
        command=save
    )

    save_button.pack(pady=20)


    status = ctk.CTkLabel(
        add_window,
        text=""
    )

    status.pack()


# -----------------------------
# View passwords
# -----------------------------

def view_passwords():

    view_window = ctk.CTkToplevel(app)

    view_window.title("Saved Passwords")

    view_window.geometry("700x500")


    title = ctk.CTkLabel(
        view_window,
        text="Saved Passwords",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=25)


    passwords = get_passwords()


    if not passwords:

        ctk.CTkLabel(
            view_window,
            text="No passwords saved yet."
        ).pack(pady=20)

        return


    for password_data in passwords:

        record_id, account, username, encrypted_password = password_data


        try:

            decrypted_password = decrypt_password(
                master_password,
                encrypted_password
            )

        except Exception:

            decrypted_password = "Unable to decrypt"


        frame = ctk.CTkFrame(
            view_window
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=10
        )


        ctk.CTkLabel(
            frame,
            text=f"Account: {account}",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=5
        )


        ctk.CTkLabel(
            frame,
            text=f"Username: {username}"
        ).pack(
            anchor="w",
            padx=15,
            pady=5
        )


        ctk.CTkLabel(
            frame,
            text=f"Password: {decrypted_password}"
        ).pack(
            anchor="w",
            padx=15,
            pady=5
        )


# -----------------------------
# Login screen
# -----------------------------

login_frame = ctk.CTkFrame(
    app
)

login_frame.pack(
    fill="both",
    expand=True
)


ctk.CTkLabel(
    login_frame,
    text="🔐 Password Manager",
    font=("Arial", 30, "bold")
).pack(pady=(100, 20))


ctk.CTkLabel(
    login_frame,
    text="Enter your master password",
    font=("Arial", 16)
).pack(pady=10)


master_entry = ctk.CTkEntry(
    login_frame,
    placeholder_text="Master password",
    show="*",
    width=350,
    height=45
)

master_entry.pack(pady=20)


unlock_button = ctk.CTkButton(
    login_frame,
    text="Unlock",
    width=200,
    height=45,
    command=unlock
)

unlock_button.pack(pady=15)


status_label = ctk.CTkLabel(
    login_frame,
    text=""
)

status_label.pack()


# -----------------------------
# Dashboard
# -----------------------------

dashboard_frame = ctk.CTkFrame(
    app
)


ctk.CTkLabel(
    dashboard_frame,
    text="🔐 Password Manager",
    font=("Arial", 30, "bold")
).pack(pady=(60, 15))


ctk.CTkLabel(
    dashboard_frame,
    text="Manage your saved passwords",
    font=("Arial", 16)
).pack(pady=(0, 40))


ctk.CTkButton(
    dashboard_frame,
    text="+ Add Password",
    width=250,
    height=50,
    command=open_add_password
).pack(pady=15)


ctk.CTkButton(
    dashboard_frame,
    text="👁 View Passwords",
    width=250,
    height=50,
    command=view_passwords
).pack(pady=15)


# -----------------------------
# Start application
# -----------------------------

app.mainloop()

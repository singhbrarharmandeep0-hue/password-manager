import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Create application window
app = ctk.CTk()

app.title("Password Manager")
app.geometry("700x450")


# Heading
title = ctk.CTkLabel(
    app,
    text="🔐 Password Manager",
    font=("Arial", 28, "bold")
)

title.pack(pady=40)


# Subtitle
subtitle = ctk.CTkLabel(
    app,
    text="Securely manage your passwords",
    font=("Arial", 16)
)

subtitle.pack(pady=10)


# Start button
start_button = ctk.CTkButton(
    app,
    text="Get Started",
    width=200,
    height=45
)

start_button.pack(pady=40)


# Start application
app.mainloop()

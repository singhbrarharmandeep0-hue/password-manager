import sqlite3


def create_database():

    connection = sqlite3.connect("password_manager.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def add_password(account, username, encrypted_password):

    connection = sqlite3.connect("password_manager.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO passwords (account, username, password)
        VALUES (?, ?, ?)
    """, (account, username, encrypted_password))

    connection.commit()

    connection.close()


def get_passwords():

    connection = sqlite3.connect("password_manager.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, account, username, password
        FROM passwords
    """)

    passwords = cursor.fetchall()

    connection.close()

    return passwords
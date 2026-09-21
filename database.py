import sqlite3


DATABASE = "password_manager.db"


def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # Password storage
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Security settings
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            salt BLOB NOT NULL,
            verifier BLOB NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def save_security_data(salt, verifier):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO settings (id, salt, verifier)
        VALUES (1, ?, ?)
    """, (salt, verifier))

    connection.commit()

    connection.close()


def get_security_data():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT salt, verifier
        FROM settings
        WHERE id = 1
    """)

    result = cursor.fetchone()

    connection.close()

    return result


def add_password(account, username, encrypted_password):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO passwords
        (account, username, password)
        VALUES (?, ?, ?)
    """, (
        account,
        username,
        encrypted_password
    ))

    connection.commit()

    connection.close()


def get_passwords():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, account, username, password
        FROM passwords
    """)

    passwords = cursor.fetchall()

    connection.close()

    return passwords
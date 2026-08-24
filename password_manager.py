from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

def derive_key(password):
    salt = b'static_salt_123'  # for learning (store securely in real apps)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

main_pwd = input("Enter the password: ")
key = derive_key(main_pwd)
fer = Fernet(key)

def view():
    try:
        with open('password.txt', 'r') as p:
            for line in p:
                line = line.strip()
                if not line:
                    continue
                try:
                    address, password_enc = line.split("|", 1)
                    password = fer.decrypt(password_enc.encode()).decode()
                except Exception as e:
                    password = f"<error decrypting: {e}>"
                print("User:", address, ", password:", password)
    except FileNotFoundError:
        print("No passwords saved yet (password.txt not found). Use 'add' to create one.")

def add():
    name = input('account name: ')
    pwd = input('enter the password: ')
    with open('password.txt', 'a') as p:
        p.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    options = input("Do you want to view or add a password? (view/add) or q to quit: ").strip().lower()
    if options == "q":
        break
    elif options == "view":
        view()
    elif options == "add":
        add()
    else:
        print('invalid option')
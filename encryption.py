import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT = b"static_salt_123"


def derive_key(master_password):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )

    return key


def create_fernet(master_password):

    key = derive_key(master_password)

    return Fernet(key)


def encrypt_password(master_password, password):

    fer = create_fernet(master_password)

    encrypted = fer.encrypt(
        password.encode()
    ).decode()

    return encrypted


def decrypt_password(master_password, encrypted_password):

    fer = create_fernet(master_password)

    decrypted = fer.decrypt(
        encrypted_password.encode()
    ).decode()

    return decrypted
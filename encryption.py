import os
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


ITERATIONS = 600000


def generate_salt():

    return os.urandom(16)


def derive_key(master_password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(
            master_password.encode()
        )
    )

    return key


def create_verifier(master_password, salt):

    key = derive_key(
        master_password,
        salt
    )

    return key


def verify_master_password(
    master_password,
    salt,
    stored_verifier
):

    try:

        key = derive_key(
            master_password,
            salt
        )

        return key == stored_verifier

    except Exception:

        return False


def encrypt_password(
    master_password,
    password,
    salt
):

    key = derive_key(
        master_password,
        salt
    )

    fer = Fernet(key)

    encrypted = fer.encrypt(
        password.encode()
    ).decode()

    return encrypted


def decrypt_password(
    master_password,
    encrypted_password,
    salt
):

    key = derive_key(
        master_password,
        salt
    )

    fer = Fernet(key)

    decrypted = fer.decrypt(
        encrypted_password.encode()
    ).decode()

    return decrypted
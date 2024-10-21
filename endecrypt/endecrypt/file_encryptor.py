from cryptography.fernet import Fernet

# Function to generate an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the encryption key from a file
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(f"{file_path}.encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{file_path}' has been encrypted.")

# Function to decrypt a file
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(f"{encrypted_file_path}.decrypted", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"File '{encrypted_file_path}' has been decrypted.")

# Example usage:
if __name__ == "__main__":
    # Generate the encryption key
    key = generate_key()

    # Encrypt a file
    encrypt_file('yourfile.txt', key)

    # Decrypt a file
    decrypt_file('yourfile.txt.encrypted', key)
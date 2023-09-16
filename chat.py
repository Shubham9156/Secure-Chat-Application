from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message, key):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    return cipher_suite.decrypt(encrypted_message).decode()

def main():
    print("Secure Chat Application")
    print("Encryption key:", key.decode())  # Display the encryption key

    while True:
        choice = input("Enter '1' to send a message, '2' to receive a message, or 'q' to quit: ")

        if choice == '1':
            message = input("You: ")
            encrypted_message = encrypt_message(message, key)
            print("Encrypted message:", encrypted_message.decode())

        elif choice == '2':
            encrypted_message = input("Enter the received encrypted message: ")
            decrypted_message = decrypt_message(encrypted_message.encode(), key)
            print("Chat Partner:", decrypted_message)

        elif choice.lower() == 'q':
            break

if __name__ == "__main__":
    main()

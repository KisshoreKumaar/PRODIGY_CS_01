def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if choice == 'encrypt':
        encrypted = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'decrypt':
        decrypted = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please select 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


print("Caesar Cipher Program")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'encrypt' or 'decrypt': ").lower()

if choice in ["encrypt", "decrypt"]:
    output = caesar_cipher(message, shift, choice)
    print("Result:", output)
else:
    print("Invalid choice")

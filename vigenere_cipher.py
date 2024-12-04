def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""  # Initialize an empty string to store the encrypted message.
    keyword = keyword.upper()  # Convert the keyword to uppercase for consistency.

    for i in range(len(plaintext)):  # Loop through each character of the plaintext.
        char = plaintext[i]  # Get the current character of the plaintext.
        if char.isalpha():  # Check if the character is alphabetic.
            shift = ord(keyword[i % len(keyword)]) - ord('A')  # Calculate the shift based on the keyword.
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))  # Encrypt the character.
            ciphertext += encrypted_char  # Append the encrypted character to the result.
        else:
            ciphertext += char  # If not alphabetic, keep the character unchanged.
    return ciphertext  # Return the encrypted message.


def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""  # Initialize an empty string to store the decrypted message.
    keyword = keyword.upper()  # Convert the keyword to uppercase for consistency.

    for i in range(len(ciphertext)):  # Loop through each character of the ciphertext.
        char = ciphertext[i]  # Get the current character of the ciphertext.
        if char.isalpha():  # Check if the character is alphabetic.
            shift = ord(keyword[i % len(keyword)]) - ord('A')  # Calculate the shift based on the keyword.
            decrypted_char = chr((ord(char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))  # Decrypt the character.
            plaintext += decrypted_char  # Append the decrypted character to the result.
        else:
            plaintext += char  # If not alphabetic, keep the character unchanged.
    return plaintext  # Return the decrypted message.


# Main program
while True:
    print("Choose an option:")  # Display the main menu to the user.
    print("1. Encrypt")
    print("2. Decrypt")
    print("3.Exit")
    choice = input("Enter your choice (1 or 2 or 3): ")  # Take the user's choice as input.


    if choice == "1":  # If the user chooses encryption.
        plaintext = input("Enter the plaintext: ")  # Ask for the plaintext.
        keyword = input("Enter the keyword: ")  # Ask for the keyword.
        ciphertext = vigenere_encrypt(plaintext, keyword)  # Encrypt the plaintext using the provided keyword.
        print("\nEncrypted text (Ciphertext):", ciphertext)  # Display the encrypted text.


    elif choice == "2":  # If the user chooses decryption.
        ciphertext = input("Enter the ciphertext: ")  # Ask for the ciphertext.
        keyword = input("Enter the keyword: ")  # Ask for the keyword.
        plaintext = vigenere_decrypt(ciphertext, keyword)  # Decrypt the ciphertext using the provided keyword.
        print("\nDecrypted text (Plaintext):", plaintext)  # Display the decrypted text.

    elif choice == "3":  # If the user chooses to exit
        print("Exiting the program. Goodbye!")  # Display a goodbye message
        break  # Exit the loop, ending the program

    else:  # If the user enters an invalid choice.
        print("Invalid choice! Please choose 1 or 2 or 3.")  # Display an error message.


# shift = ord(keyword[i % len(keyword)]) - ord('A')

# ord(char): This function returns the Unicode code point for a character. For example, ord('A') returns 65, and ord('B') returns 66.
# keyword[i % len(keyword)]: The keyword is repeated or truncated to match the length of the plaintext. i % len(keyword) ensures that the keyword repeats if it's shorter than the plaintext. For example, if the keyword is "KEY" and the plaintext is "HELLO", this part makes sure "KEY" repeats for each character of the plaintext (i.e., "KEYKE").
# ord(keyword[i % len(keyword)]) - ord('A'): This calculates the numerical position of the character in the alphabet. For example:
# ord('K') - ord('A') = 75 - 65 = 10 (So, the shift for 'K' is 10).
# This step calculates how many positions to shift based on the current keyword character.
# encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))

# char.upper(): Converts the current character to uppercase to maintain consistency since the Vigenère cipher usually works on uppercase characters.
# ord(char.upper()) - ord('A'): This gives the position of the plaintext character in the alphabet. For example:
# ord('H') - ord('A') = 72 - 65 = 7 (So, 'H' is at position 7).
# (ord(char.upper()) - ord('A') + shift): This adds the shift (calculated from the keyword) to the position of the current character. This is the core operation of the Vigenère cipher: shifting the character by a certain number of positions.
# % 26: The modulo operation ensures that if the result exceeds 'Z' (i.e., 25), it wraps around back to 'A'. For example, if the calculation results in 30, the modulo operation converts it back to 4, which corresponds to 'E'.
# chr(... + ord('A')): After the shift, the number is converted back into a character using chr(), and ord('A') ensures the result is an alphabetic character.

import string

def caesar_cipher(text, shift):
    """
    Encrypts text by shifting alphabetical characters by a specified 
    integer while preserving casing and non-alphabet characters.
    """
    shift = shift % 26
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = []
    
    for char in text:
        if char in alphabet_lower:
            idx = alphabet_lower.index(char)
            new_idx = (idx + shift) % 26
            result.append(alphabet_lower[new_idx])
        elif char in alphabet_upper:
            idx = alphabet_upper.index(char)
            new_idx = (idx + shift) % 26
            result.append(alphabet_upper[new_idx])
        else:
            # Preserve spaces, punctuation, numbers, and symbols
            result.append(char)
            
    return "".join(result)


def caesar_decipher(ciphertext, shift):
    """
    Decrypts a Caesar-encrypted string by shifting characters backwards.
    Returns the original clear text.
    """
    return caesar_cipher(ciphertext, -shift)


def letter_frequency(text):
    """
    Counts how many times each letter of the alphabet appears in text,
    ignoring case and non-alphabetic characters.
    
    Returns a dictionary mapping lowercase letters ('a'-'z') to their counts.
    """
    frequency = {char: 0 for char in string.ascii_lowercase}
    
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
            
    return frequency


def display_frequency(freq):
    """Prints a clean table of letter counts and percentages."""
    total_letters = sum(freq.values())
    
    if total_letters == 0:
        print("\n  [No alphabetic characters found to analyze]")
        return

    print(f"\n  Total letters analyzed: {total_letters}")
    print(f"  {'Letter':<8}{'Count':<8}{'Percentage':<10}")
    print("  " + "-" * 26)
    
    for letter, count in freq.items():
        if count > 0:  # Display only letters present in the message
            percentage = (count / total_letters) * 100
            print(f"    {letter.upper():<6}  {count:<6}  {percentage:>6.2f}%")


def main():
    """Terminal menu for encrypting, analyzing, and deciphering messages."""
    while True:
        print("\n==============================================")
        print("    CAESAR CIPHER & FREQUENCY ANALYZER TOOL   ")
        print("==============================================")
        print("1. Process Message (Encrypt, Analyze & Decrypt)")
        print("2. Exit")
        
        choice = input("\nSelect an option (1-2): ").strip()
        
        if choice == "1":
            message = input("\nEnter your message: ")
            
            try:
                shift = int(input("Enter shift value (integer): "))
            except ValueError:
                print("\nError: Shift must be a valid integer.")
                continue

            # 1. Encrypt text
            encrypted_text = caesar_cipher(message, shift)
            
            # 2. Analyze letter frequency on original message
            freq_data = letter_frequency(message)
            
            # 3. Decrypt text back
            decrypted_text = caesar_decipher(encrypted_text, shift)

            # Display results
            print("\n" + "=" * 46)
            print("                   RESULTS                    ")
            print("=" * 46)
            print(f"\nOriginal Message : {message}")
            print(f"Shift Value      : {shift}")
            print(f"Ciphered Text    : {encrypted_text}")
            print(f"Deciphered Text  : {decrypted_text}")
            
            print("\n--- Letter Frequency Breakdown ---")
            display_frequency(freq_data)

        elif choice == "2":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid selection. Please choose 1 or 2.")


if __name__ == "__main__":
    main()

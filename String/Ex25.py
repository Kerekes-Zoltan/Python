"""
Write a Python program to create a Caesar encryption.
"""

def caesar_encrypt(plaintext, shift):
    
    encrypted_text = ""
    
    for char in str:
        if char.isalpha():
            shift_base = ord('A') if char.isupper()else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_char = char #Keep non-alphabetic characters unchanged
        
        encrypted_text += encrypted_char
        
    return encrypted_text

plaintext = input("Enter text to encrypt: ")
shift_value = int(input("Enter shift value: "))

encrypted_text = caesar_encrypt(plaintext, shift_value)
print(f"Encrypted text: {encrypted_text}")
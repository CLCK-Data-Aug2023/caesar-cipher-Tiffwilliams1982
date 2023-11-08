def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha(): 
            is_upper = char.isupper() 
            char = char.lower()  
            shifted = ord(char) + shift - ord('a')  
            shifted = shifted % 26  
            shifted += ord('a')  
            if is_upper:  
                char = chr(shifted).upper()
            else:
                char = chr(shifted)
        encrypted_text += char

    return encrypted_text

# Example usage:
text = "My name is Tiffany!"
shift = 2
encrypted_text = caesar_cipher(text, shift)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)


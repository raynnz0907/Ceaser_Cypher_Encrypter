FIRST_CODE_SHIFT = ord("A")
LAST_CODE_SHIFT = ord("Z")
CODE_RANGE = 26


def ceaser_code(message, shift):
    # Result place holder.
    result = ""
    # Going through each letters of the string
    for char in user_message.upper():    
        if char.isalpha():
            char_code = ord(char)          # Converting alphabets to ASCII key
            code_shift = char_code + shift

            if code_shift > LAST_CODE_SHIFT:   # Checks if the key is going beyond letter "Z"
                code_shift -= CODE_RANGE

            if code_shift < FIRST_CODE_SHIFT:  # Checks if the key is below letter "A"
                code_shift += CODE_RANGE

            char_convert = chr(code_shift)     # Converting ASCII key back to alphabets
            result += char_convert             # Storing the ceaser code in the empty string holder
        else:
            result += char           
    return result


user_message = input("Enter the sentence you want to encrypt: ")
user_shift = int(input("Enter the key you want: "))

print(ceaser_code(user_message, user_shift))




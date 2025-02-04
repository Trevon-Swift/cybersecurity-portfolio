message = "Hello, World!"
shift = 7

    # Result placeholder
result = ""
# Go through each of the letters in the message.
for char in message:
    # Do something.
    char_code = ord(char)

    new_char_code = char_code + shift

    new_char = chr(new_char_code)

    print(char, char_code, new_char_code, new_char)

     

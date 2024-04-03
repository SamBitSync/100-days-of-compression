def encode(input_string):
    if not input_string:
        return ""
    
    encoded_string = ""
    last_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == last_char:
            count +=1
        else:
            encoded_string += last_char + str(count)
            last_char = char
            count = 1
    
    encoded_string += last_char + str(count)
    return encoded_string

def decode(encoded_string):
    decoded_string = ""
    char_index = 0

    while char_index < len(encoded_string):
        char = encoded_string[char_index]
        count = ""
        char_index += 1

        while char_index < len(encoded_string) and encoded_string[char_index].isdigit():
            count += encoded_string[char_index]
            char_index += 1

            decoded_string += char * int(count)
    return decoded_string


original_string = "RIIMALLLLL"
encoded_string = encode(original_string)
decoded_string = decode(encoded_string)

print(f"Original: {original_string}")
print(f"Encoded: {encoded_string}")
print(f"Decoded: {decoded_string}")

    

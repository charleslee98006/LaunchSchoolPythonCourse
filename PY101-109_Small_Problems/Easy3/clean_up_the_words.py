def clean_up(text):
    non_alpha_occur_in_row = False
    result = ''
    for character in text:
        if character.isalpha():
           result += character
           non_alpha_occur_in_row = False
        else:
            if not non_alpha_occur_in_row:
                result += ' '
                non_alpha_occur_in_row = True
    return result

print(clean_up("---what's my +*& line?") == " what s my line ") # True
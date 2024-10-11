def print_in_box(text):
    if isinstance(text, str):
        for row in range(0, 5):
            box_maker = ''        
            for i in range(0, len(text) + 4):
                if i == 0 or (i == len(text) + 3):
                    if row == 0 or row == 4:
                        box_maker += '+'
                    else:
                        box_maker += '|'
                elif i > 0 or (i < len(text) + 3):
                    if row == 0 or row == 4:
                        box_maker += '-'
                    elif row == 1 or row == 3:
                        box_maker += ' '
                    elif row == 2:
                        box_maker += ' '
                    

            print(box_maker)
    else:
        print('Please use a string thanks!')
print_in_box('')
# print_in_box('To boldly go where no one has gone before.')
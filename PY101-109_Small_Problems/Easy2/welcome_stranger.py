def greetings(full_name_list, title_occupation_dict):
    if isinstance(full_name_list, list) and isinstance(title_occupation_dict, dict):
        if (len(full_name_list) == 3) and (len(title_occupation_dict) == 2):
            return 'Hello, {} {} {}! Nice to have a {} {} around.'.format(
                    full_name_list[0], full_name_list[1], full_name_list[2], title_occupation_dict['title'], title_occupation_dict['occupation'])
        else:
            return 'Please use a list and a dictionary with the appropriate lengthes.'
    else:
        return 'Please use a list and a dictionary for the parameters.'

# Test cases:
greeting = greetings(["John", "Q", "Doe"], {"title": "Master", "occupation": "Plumber"},)
print(greeting) #prints out 'Hello, John Q Doe! Nice to have a Master Plumber around'.
greeting = greetings([], {},)
print(greeting) #prints out 'Please use a list and a dictionary with the appropriate lengthes.'
greeting = greetings(["John", "Q", "Doe", "something"], {"title": "Master", "occupation": "Plumber"},)
print(greeting) #prints out 'Please use a list and a dictionary with the appropriate lengthes.'
greeting = greetings(["John", "Q", "Doe",], {"title": "Master", "occupation": "Plumber", "occupation2": "Uber driver"},)
print(greeting) #prints out 'Please use a list and a dictionary with the appropriate lengthes.'
greeting = greetings(12.1,  {"title": "Master", "occupation": "Plumber", "occupation2": "Uber driver"},)
print(greeting) #prints out 'Please use a list and a dictionary for the paramters.'
greeting = greetings(["John", "Q", "Doe",],  None)
print(greeting) #prints out 'Please use a list and a dictionary for the paramters.'
def staggered_case(text):
    toggle = True
    new_list = []
    for char in text:
        if(char.isalpha()):
            if(toggle):
                new_list.append(char.upper())
                toggle = False
            else:
                new_list.append(char.lower())
                toggle = True
        else:
            new_list.append(char)
    return ''.join(new_list)


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
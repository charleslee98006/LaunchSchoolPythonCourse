def short_long_short(string1, string2):
    if(isinstance(string1, str) and isinstance(string2, str)):
        result = ''
        if len(string1) < len(string2):
            result = string1 + string2 + string1
        elif len(string1) > len(string2):
            result = string2 + string1 + string2
        else:
            raise ValueError(f'"{string1}" and \"{string2}\" are same length. Please give a different length strings')
        return result
    else:
        raise ValueError('Please enter string values for argument 1 and argument 2')

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc") # print True
print(short_long_short('abcde', 'fgh') == "fghabcdefgh") # print True
print(short_long_short('', 'xyz') == "xyz") # print True
# print(short_long_short('', '') == "") # print ValueError: "" and "" are same length. Please give a different length strings
print(short_long_short(1.20, None) == "") # print ValueError: Please enter string values for argument 1 and argument 2
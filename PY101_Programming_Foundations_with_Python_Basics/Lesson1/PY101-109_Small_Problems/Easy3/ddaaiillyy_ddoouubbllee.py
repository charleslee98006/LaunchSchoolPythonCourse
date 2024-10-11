def crunch(text):
    if isinstance(text, str):
        result = ''
        if text:
            index_not_dup = ''
            for char in text:
                if not char == index_not_dup:
                    result += char
                    index_not_dup = char
            return result
        else:
            return result

    else:
        print('Please select a string greeting and a integer value for repeat')
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
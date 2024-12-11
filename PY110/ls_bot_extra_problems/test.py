def is_prime(number):
    if(number == 1):
        return False
    for i in range(2, int(number**0.5) + 1):
        # print(i)
        # print(number % i)
        if(number % i != 1):
            return False
    return True

def prime_count(text):
    unique_char = set(text.lower())
    # print(unique_char)
    dictionary = {char: text.lower().count(char) for char in unique_char if is_prime(text.lower().count(char))}
    # print(dictionary)
    new_list = [ character for character in dictionary.keys()]
    # print(new_list)
    new_string = []
    for each in new_list:
        new_list.append(each.upper())
    # print(new_string)
    for letter in text:
        if letter in new_list:
            new_string.append(letter)
    print(''.join(new_string))
    return ''.join(new_string)

    

# is_prime(12)
# print(prime_count("abc") == "")
# print(prime_count("abbcccdddd") == "bbccc")
print(prime_count("bbbbBBB") == "bbbbBBB")
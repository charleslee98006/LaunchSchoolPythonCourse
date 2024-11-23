# - input
#     - string arg
# - output
#     - string arg
# Explicit Rules
# - every second character in every third word uppercase
# - other characters remain the same


def to_weird_case(text):
    text_array = text.split()
    new_list = []
    for index in range(len(text_array)):
        changed_word = ''
        for index2 in range(len(text_array[index])):
            if (index + 1) % 3 == 0 and index2 % 2 == 1:
                changed_word += text_array[index][index2].upper()
            else:
                changed_word += text_array[index][index2]
        new_list.append(changed_word)        
    return ' '.join(new_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
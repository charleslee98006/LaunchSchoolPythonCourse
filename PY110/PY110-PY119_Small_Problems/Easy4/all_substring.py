def substrings(text):
    return [text[index1:index2] for index1 in range(0, len(text)+1) for index2 in range(index1+1, len(text)+1)]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
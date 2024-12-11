#Problem
# -Input
#     - list of strings
# -Output
#     - nested list where inner list of words that combination of words from the same characters
# - Explicit Rules
#     - anagrams words formed by rearranging letters from another word
# - Implicit Rules

# #Examples

#     # Test case 1: Simple anagrams
#     result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#     expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
#     print("Test case 1:")
#     print(f"Expected: {sorted(expected)}")
#     print(f"Got: {sorted(result)}")
#     print("Passed" if sorted(result) == sorted(expected) else "Failed")
#     print()

# # Test case 2: No anagrams
# result = group_anagrams(["hello", "world", "python"])
# expected = [["hello"], ["world"], ["python"]]
# print("Test case 2:")
# print(f"Expected: {sorted(expected)}")
# print(f"Got: {sorted(result)}")
# print("Passed" if sorted(result) == sorted(expected) else "Failed")
# print()

# # Test case 3: Empty list
# result = group_anagrams([])
# expected = []
# print("Test case 3:")
# print(f"Expected: {expected}")
# print(f"Got: {result}")
# print("Passed" if result == expected else "Failed")
# print()

# # Test case 4: Single character anagrams
# result = group_anagrams(["a", "b", "c", "a"])
# expected = [["a", "a"], ["b"], ["c"]]
# print("Test case 4:")
# print(f"Expected: {sorted(expected)}")
# print(f"Got: {sorted(result)}")
# print("Passed" if sorted(result) == sorted(expected) else "Failed")
# print()

# # Test case 5: Anagrams with different cases
# result = group_anagrams(["Rat", "Car", "Below", "Taste", "Cried", "Study", "Thing", "Chin", "Rat", "Arc", "Elbow"])
# expected = [["Rat", "Rat"], ["Car", "Arc"], ["Below", "Elbow"], ["Taste"], ["Cried"], ["Study"], ["Thing"], ["Chin"]]
# print("Test case 5:")
# print(f"Expected: {sorted(expected)}")
# print(f"Got: {sorted(result)}")
# print("Passed" if sorted(result) == sorted(expected) else "Failed")
# print()


#Data Structures
# - set to get the unique characters and then a dictionary to get count

# #Algo
# def group_anagrams(list1):
#     1. go through each word in the list and get the count of each letter in word:
#         1. if match and not in list  - add to the list
#Code
def group_anagrams(list1):
    result_dict = {}
    for word in list1:
        inner_list = []
        new_dict = {letter: word.count(letter) for letter in set(word)}
        # print(new_dict)
        signature = ''
        for key, value in new_dict.items():
            signature += (key + str(value))
        signature = ''.join(sorted(signature.lower()))
        # print(signature)
        if result_dict.get(signature) == None:
            result_dict.setdefault(signature, [])
        result_dict[signature].append(word)
    # print(list(result_dict.values()))
    return list(result_dict.values())
        
def test_group_anagrams():
    def check_result(result, expected, case_num):
        print(f"Test case {case_num}:")
        print(f"Expected (any order): {expected}")
        print(f"Got: {result}")
        
        result_set = set(tuple(sorted(group)) for group in result)
        expected_set = set(tuple(sorted(group)) for group in expected)
        print("Passed" if result_set == expected_set else "Failed")
        print()

    # Test case 1: Simple anagrams
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
    check_result(result, expected, 1)

    # Test case 2: No anagrams
    result = group_anagrams(["hello", "world", "python"])
    expected = [["hello"], ["world"], ["python"]]
    check_result(result, expected, 2)

    # Test case 3: Empty list
    result = group_anagrams([])
    expected = []
    check_result(result, expected, 3)

    # Test case 4: Single character anagrams
    result = group_anagrams(["a", "b", "c", "a"])
    expected = [["a", "a"], ["b"], ["c"]]
    check_result(result, expected, 4)

    # Test case 5: Anagrams with different cases
    result = group_anagrams(["Rat", "Car", "Below", "Taste", "Cried", "Study", "Thing", "Chin", "Rat", "Arc", "Elbow"])
    expected = [["Rat", "Rat"], ["Car", "Arc"], ["Below", "Elbow"], ["Taste"], ["Cried"], ["Study"], ["Thing"], ["Chin"]]
    check_result(result, expected, 5)

# Run the tests
test_group_anagrams()
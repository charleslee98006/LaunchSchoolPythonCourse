def repeat(text, repeats):
    if isinstance(text, str) and isinstance(repeats, int):
        for _ in range(repeats):
            print(text)
    else:
        print('Please select a string greeting and a integer value for repeat')

repeat('Hello', 3)
repeat(' ', 3)
repeat(None, 3)
repeat('3', None)
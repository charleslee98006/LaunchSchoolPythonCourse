def swap_name(text):
    return  f'{text.split()[1]}, {text.split()[0]}'


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

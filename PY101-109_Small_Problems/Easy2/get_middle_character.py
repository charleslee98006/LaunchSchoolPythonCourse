def center_of(text):
    return text[(len(text) // 2)] if len(text) % 2 else text[(len(text) // 2) - 1 : (len(text) // 2) + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
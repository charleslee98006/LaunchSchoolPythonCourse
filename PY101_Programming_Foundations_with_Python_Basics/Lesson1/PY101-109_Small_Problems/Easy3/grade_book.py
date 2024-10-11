def get_grade(grade1, grade2, grade3):
    mean  = (grade1 + grade2 + grade3) / 3
    match mean:
        case mean if mean >= 90:
            return "A"
        case mean if mean >= 80:
            return "B"
        case mean if mean >= 70:
            return "C"
        case mean if mean >= 60:
            return "D"
        case mean if mean >= 50:
            return "F"
        case _:
            raise ValueError('Please enter values between 0 to 100')

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
def AgeIncrease(age, increment):
    for i in range(1,5):
        number_of_age_increase = (increment*i)
        print(f'In {number_of_age_increase} years, you will be {age + number_of_age_increase} years old.')      
AgeIncrease(22, 10)
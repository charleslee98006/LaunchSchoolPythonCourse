import datetime
def when_will_you_retire():
    while True:
        current_age = input('What is your age? ')
        retiring_age = input('At what age would you like to retire? ')
        if(isinstance(current_age, str) and isinstance(retiring_age, str)):
            difference = int(retiring_age) - int(current_age)
            print(f'It\'s {datetime.date.today().year}, you will retire in {datetime.date.today().year + difference}')
            print(f'You have only {difference} years of work to go!')
            break
        else:
            print('Please enter in a Integer value for both questions.')
    
when_will_you_retire()
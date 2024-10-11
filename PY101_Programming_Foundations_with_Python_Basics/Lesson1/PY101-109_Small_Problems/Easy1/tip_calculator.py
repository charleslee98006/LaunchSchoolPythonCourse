def tip_calculator():
    while True:
        bill = input('What is the bill? ')
        percentage = input('What is the tip precentage? ')
        if is_float(bill) and is_float(percentage):
            bill = float(bill)
            percentage = float(percentage)
            tip = (percentage/100) * bill
            total = bill + tip
            print(f'The tip is ${tip:0.2f}\nThe total is ${total:0.2f}')
            break
        else:
            print('Please use integers only. Please try again:\n')

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

tip_calculator()
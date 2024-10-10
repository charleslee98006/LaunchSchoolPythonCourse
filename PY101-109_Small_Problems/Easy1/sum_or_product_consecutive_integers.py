def sum_product_consecutive_integers():
    prompt1 = input('Please enter an integer greater than 0: ')
    prompt2 = input('Enter "sum" to compute the sum, or "product" to compute the product: ')
    if prompt1.isnumeric() and int(prompt1) > 0: 
        if prompt2 == 'sum' or prompt2 == 'product':
            total = 1
            for number in range(1, int(prompt1) + 1):
                if prompt2 == 'sum':
                    total += number
                else:
                    total *= number
            print(f'The {prompt2} of the integers between 1 and {prompt1} is {total}.')
        else:
            print(f'Please enter "product" or "sum" words only.')
    else:
        print(f'Please enter an integer that is greater than zero.')
        
sum_product_consecutive_integers()

# Test Case 1:
# Please enter an integer greater than 0: 0
# Enter "sum" to compute the sum, or "product" to compute the product: sum
# Answer: Please enter an integer that is greater than zero.

# Test Case 2:
# Please enter an integer greater than 0: 1
# Enter "sum" to compute the sum, or "product" to compute the product: s
# Answer: Please enter "product" or "sum" words only.

# Test Case 3:
# Please enter an integer greater than 0: 1
# Enter "sum" to compute the sum, or "product" to compute the product: sum
# Answer: The sum of the integers between 1 and 1 is 2.

# Test Case 4:
# Please enter an integer greater than 0: 1
# Enter "sum" to compute the sum, or "product" to compute the product: product
# Answer: The product of the integers between 1 and 1 is 1.

# Test Case 5:
# Please enter an integer greater than 0: -1
# Enter "sum" to compute the sum, or "product" to compute the product: sum
# Please enter an integer that is greater than zero.

# Test Case 6:
# Please enter an integer greater than 0: 1.0
# Enter "sum" to compute the sum, or "product" to compute the product: si,
# Please enter an integer that is greater than zero.
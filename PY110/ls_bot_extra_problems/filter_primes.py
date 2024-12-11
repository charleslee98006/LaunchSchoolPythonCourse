def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            return False
    return True

def filter_primes(numbers):
    prime_list = [each for each in numbers if is_prime(each)]
    # print(prime_list)
    return prime_list

# Test cases
print(filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7])
print(filter_primes([10, 12, 14, 16, 18, 19, 20]) == [19])
print(filter_primes([1, 4, 6, 8, 9, 10]) == [])
from math import sqrt

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))



# Check prime number
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3 :
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        
    return True

# print(is_prime(6888998))

def find_prime_number_in_range(num1, num2):
    have_prime = False
    for i in range(num1, num2+1):
        if is_prime(i):
            print(i)
            have_prime = True

    if not have_prime:
        print('No prime numbers')

find_prime_number_in_range(num1, num2)
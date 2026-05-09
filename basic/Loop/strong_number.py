# Strong number is a number in which the sum of the factorial of digits is equal to the number itself.
# 145 => 1! + 2! + 5! => 145


# write your code here

number = int(input('Enter number:- '))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    fact = 1
    for i in range(2, num+1):
        fact = fact * i

    return fact

# print(factorial(number))


def is_strong_number(num):
    n = num
    
    if num == 0 or num == 1 or num == 2:
        print('Strong Number')
        return
    
    total = 0
    while n:
        total = total + factorial(n%10)
        n = n // 10

    if total == num:
        print('Strong Number')
    else:
        print('Not Strong Number')

is_strong_number(number)

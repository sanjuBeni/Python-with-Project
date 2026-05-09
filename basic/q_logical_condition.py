# Q1. Find big number from two given number

first = float(input('Enter first number: '))
second = float(input('Enter second number: '))

# def find_greater_num(first, second):
#     if first > second:
#         print(f'First number is {first}, & greater than {second}')
#     elif second > first:
#         print(f'Second number is {second}, & greater than {first}')
#     else:
#         print('Both are equal')

# find_greater_num(first=first, second=second)

# Check Number is Positive, Negative, & Zero
num = int(input())
def check_number_type(num):
    if num < 0:
        print('Negative')
    elif num > 0:
        print('Positive')
    else:
        print('Zero')
check_number_type(num)



# Check voter age
person_age = int(input())
def is_eligible_to_vote(age):
    print('Eligible to vote') if age >= 18 else print('Not eligible to vote')
is_eligible_to_vote(person_age)

# Character is exist given string
string = input()
def exit_character(char, string):
    if char in string:
        print(f'{char} found')
    else:
        print(f'{char} not found')    
exit_character('a', string)

# check number is multiply by n
number = int(input())
def is_multiply_by(n, number):
    print(f'Multiple of {n}') if number % n == 0 else print(f'Not a multiple of {n}')

is_multiply_by(7, number)


# Find number in range
number = int(input())
def in_range(number, low = 1, high = 100):
    print('Within Range') if number >= low and number <= high else print('Out of Range')

in_range(number)

# Reverse a number
number = int(input())
def number_reverse(number):
    new_number = int(str(number)[::-1])
    # n = number
    # new_number = 0
    # while n:
    #     mod = n % 10
    #     new_number = new_number * 10 + mod
    #     n = n // 10
    
    print(new_number)

number_reverse(number)
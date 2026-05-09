# Harshad number is a number that divisible by sum of digit

number = int(input('Enter number :- '))

def harshed_number(num):
    n = abs(num)
    if n == 0:
        print('Not Harshad Number')
        return
    s = 0
    while n:
        s = s + (n % 10)
        n = n // 10

    if num % s == 0:
        print('Harshad Number')
    else:
        print('Not Harshad Number')

harshed_number(number)
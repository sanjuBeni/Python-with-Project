# write your code here
number = int(input())

def count_even_odd_digit(number) :
    n = number if number >= 0 else -(number)
    even_digit = 0
    odd_digit = 0
    if number == 0:
        print(f'Even: {1}')
        print(f'Odd: {odd_digit}')
        return
    while n:
        mod = n % 10
        if mod % 2 == 0:
            even_digit += 1
        else:
            odd_digit += 1
        n = n // 10

    print(f'Even: {even_digit}')
    print(f'Odd: {odd_digit}')

count_even_odd_digit(number)
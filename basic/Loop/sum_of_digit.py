number = int(input('Enter number: '))

def number_digit_sum(num):
    n = num
    total = 0
    while n:
        mod = n % 10
        total = total + mod
        n = n // 10

    return total

print(number_digit_sum(num=number))
# write your code here
number = int(input('Enter number :- '))

def digit_product(num):
    n = abs(num)
    if n == 0:
        print(0)
    prod = 1
    while n > 0:
        prod = prod * (n % 10)
        n = n//10

    print(prod)

digit_product(number)

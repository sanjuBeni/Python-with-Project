# write your code here
from math import sqrt
number = int(input())

def number_factor(number):
    if number < 0:
        return 
    if number == 1:
        print(number)
    factors = []
    for i in range(1, int(sqrt(number)) + 1) :
        if number % i == 0:
            factors.append(i)
            if number // i != i:
                factors.append(number // i)
    
    print(' '.join([str(f) for f in sorted(factors)]))

number_factor(number)



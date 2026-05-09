# write your code here
from math import sqrt

num1 = int(input())
num2 = int(input())

def find_factor(num):
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)

    
    return ' '.join([str(i) for i in sorted(factors)])

for i in range(num1, num2+1):
    print(find_factor(i))

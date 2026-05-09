from math import sqrt

# num1 = int(input('Enter number1 : '))
# num2 = int(input('Enter number2 : '))

# for num in range(num1, num2 + 1):
#     if num > 0 :
#         root = int(sqrt(num))
#         if num == root * root:
#             print(num, end=" ")


sum_of_number = 0
total_number = 0
is_zero = False
while True:
    num = int(input())
    if num <= 0:
        # print(num)
        break
    sum_of_number += num
    total_number += 1

print(sum_of_number/total_number)



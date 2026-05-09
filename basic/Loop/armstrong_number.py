# negative numbers are NOT Armstrong numbers

# write your code here
number = int(input())

def check_armstrong(number):
    if number < 0:
        print('Not Armstrong')
        return
    if number == 0:
        print('Armstrong')
        return
    n = str(number)
    len_num = len(n)
    new_num = 0
    for num in n:
        new_num = new_num + (int(num) ** len_num)

    print('Armstrong') if new_num == number else print('Not Armstrong')

check_armstrong(number)


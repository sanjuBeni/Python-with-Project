# Most definitions of palindromes only apply to positive numbers 

# write your code here
num_str = input()
split_str = num_str.split(' ')
num1 = int(split_str[0])
num2 = int(split_str[1])

def is_palindrome(num):
    n = num[::-1]
    return n == num

def find_palindrome_in_range(num1, num2):
    palindrome_nums = []
    for num in range(num1, num2 + 1):
        if is_palindrome(str(num)):
            palindrome_nums.append(str(num))

    print(' '.join(palindrome_nums))

find_palindrome_in_range(num1, num2)




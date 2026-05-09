number = int(input('find largest digit of a number:- '))

def largest_digit_in_number(number) :

    large_digit = 0
    n = str(abs(number))
    for i in range(len(n)) :
        digit = int(n[i])
        if not (large_digit > digit) :
            large_digit = digit
    
    print(large_digit)

largest_digit_in_number(number)

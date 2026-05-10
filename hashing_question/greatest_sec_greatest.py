
lst = [10, 5, 8, 20, 15]

lst = [5, 5]

def find_two_greatest_nums(lst:list[int])->list:
    n = len(lst)
    if n < 2:
        return lst

    large = 0
    large_2nd = 0

    for num in lst:
        if large < num:
            large_2nd = large
            large = num
        elif large_2nd < num and large != num:
            large_2nd = num


    return [large, large_2nd]

print(find_two_greatest_nums(lst))
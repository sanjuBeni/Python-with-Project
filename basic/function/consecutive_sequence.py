

"""
    Skip duplicate value
    

"""



def longest_consecutive(nums):
    if not nums:
        return 0, [] # It means (0, []) tuple return
    numbers = sorted(nums) 

    longest = 1
    current_length = 1

    for n in range(1, len(numbers)):
        # Skips Duplicate
        if numbers[n] == numbers[n-1]:
            continue

        # Check if consecutive
        if numbers[n] == numbers[n-1] + 1:
            current_length += 1
        else:
            longest = max(longest, current_length)
            current_length = 1

    return max(longest, current_length)


print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

nums = [1100, 45, 5, 9, 98, 50, 3, 400, 5, 8]

def large_2nd_element(nums):
    if not nums:
        return 0, []
    
    large1 = 0
    lerge2 = 0
    for n in nums:
        if n > large1:
            large2 = large1
            large1 = n
        elif n > large2:
            large2 = n

    return large2

print(large_2nd_element(nums))


# def large_num(nums):
#     if not nums:
#         return 0, []
    
#     large = nums[0]
#     index = 0
#     for i in range(len(nums)):
#         if large < nums[i]:
#             large = nums[i]
#             index = i

#     return index, large

# index, large = large_num(nums)

# nums.pop(index)

# index, large = large_num(nums)
# print(f"2nd largest element is {large}")
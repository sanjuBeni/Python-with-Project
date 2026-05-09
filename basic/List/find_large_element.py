
nums = [110, 45, 5, 9, 98, 50, 3, 400, 5, 8]

def find_large_num(nums):
    if not nums:
        return 0, []
    
    large_num = nums[0]
    index = 0
    for i in range(1, len(nums)):
        if nums[i] > large_num:
            index = i
            large_num = nums[i]

    print(f"Largest element on {index} index.")
    return large_num

print(find_large_num(nums))

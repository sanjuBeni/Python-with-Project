
nums = [10, 20, 30, 40, 50]

def left_rotation(nums):
    if not nums:
        return 0, []
    
    for i in range(len(nums) - 1):
        # Swap value
        nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

print(left_rotation(nums=nums))


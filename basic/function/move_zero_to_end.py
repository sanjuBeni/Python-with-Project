def move_zeros_to_end(nums):
    if not nums:
        return 0, []

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums

print(move_zeros_to_end([1, 0, 0, 2, 0, 3, 0, 4]))
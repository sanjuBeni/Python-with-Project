
# nums = [0, 1, 2, 2, 4, 4, 1]

# nums = [4, 4, 4, 9, 2, 4]
nums = [1, 2, 3, 45, 5, 6]

def find_list_even_num_appeare(nums:list[int])->int|None:
    if not nums:
        return []
    
    for i in range(len(nums) -1):
        if nums[i] % 2 == 0 and nums[i+1] % 2 == 0:
            return nums[i]
        
    return -1

print(find_list_even_num_appeare(nums))
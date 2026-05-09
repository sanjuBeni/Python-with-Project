
def find_pair_with_sum(nums, target):
    if not nums:
        return 0, []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                return f"{nums[i]} {nums[j]}"
            
    return f"{-1} {-1}"

# find_pair_with_sum()

[].insert()
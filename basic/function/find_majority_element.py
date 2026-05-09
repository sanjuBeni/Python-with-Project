
def find_majority_element(nums):
    if not nums:
        return 0, []
    
    mk_dict = {}
    for n in nums:
        mk_dict[n] = mk_dict.get(n, 0) + 1
    
    max_value = max(mk_dict.values())
    max_value_key = max(mk_dict.values(), key=mk_dict.get)
    return max_value_key if max_value > len(nums) / 2 else -1

print(find_majority_element([1,2,3,1,1]))
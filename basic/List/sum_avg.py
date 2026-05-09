
list_data = [1,2,3,4,5]

def list_element_sum(nums):
    if not nums:
        return 0, []
    
    total = 0
    for n in nums:
        total += n
    
    return total

total = list_element_sum(list_data)
print(f"Sum of list element: {total}")
print(f"Avg. : {total/len(list_data)}")
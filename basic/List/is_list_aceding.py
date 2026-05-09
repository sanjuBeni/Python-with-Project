
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def is_list_acending(nums):
    if not nums:
        return 0, []
    
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1]:
            continue
        else:
            print('List is not ascending order')
            break
    else:
        print('List is ascending order')

is_list_acending(nums)
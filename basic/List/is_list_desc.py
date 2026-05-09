
nums = [100, 90, 80, 70, 60, 50]

def is_list_desc(nums):
    if not nums:
        return 0, []
    
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            continue
        else:
            print('List is not desc order')
            break
    else:
        print('List is desc order')

is_list_desc(nums)
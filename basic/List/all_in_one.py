
# 1.    Sum and Average
# nums = [10, 20, 30, 40, 50]
# total = 0
# for n in nums:
#     total += n
# print(f"Sum of list elements is: {total}, and average is {total/len(nums)}")

# 2.    Find list largest element
# nums = [90, 500, 600, 2, 1, 4, 500, 900]
# large = nums[0]
# for i in range(1, len(nums)):
#     if nums[i] > large:
#         large = nums[i]
# print(f"Largest element of list is : {large}")


# 3.    Find 2nd largest element form list
# nums = [9001, 5000, 600, 2, 1, 4, 5001, 9000]
# large1 = nums[0]
# large2 = nums[0]
# for i in range(len(nums)):
#     if nums[i] > large1:
#         large2 = large1
#         large1 = nums[i]
#     elif nums[i] > large2:
#         large2 = nums[i] 
# print(f"Largest element is {large1}, and 2nd largest element is {large2}")


# 3.    Is list is accending order
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         continue
#     else:
#         print('List is not acending order...')
#         break
# else:
#     print('List is acending order...')


# Swap in python
# a = 10
# b = 20
# a, b = b, a
# print(a, b)


# 4.    List rotate to left 
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# first = nums[0]
# for i in range(len(nums)-1):
#     nums[i], nums[i+1] = nums[i+1], nums[i]
#     # nums[i+1] = first
# print(nums)





lst = [10,20,30,10,20,50,20]

def remove_duplicate(lst):
    if not lst:
        return lst
    return sorted(list(set(lst)))

print(remove_duplicate(lst))



# Check list elements are unique or not
def check_unique_elements(numbers):
    # Write your code here
    if not numbers:
        return []

    set1 = set(numbers)
    new_list = sorted(list(set1))

    return 'Unique' if new_list == sorted(numbers) else 'Not Unique'


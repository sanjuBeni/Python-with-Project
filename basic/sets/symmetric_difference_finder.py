
def symmetric_difference_finder(set1, set2):
    if not set1 or not set2:
        return set1
        
    return set1.symmetric_difference(set2)

set1 = {1,2,3,4}
set2 = {5,6,3,4}
print(symmetric_difference_finder(set1, set2))
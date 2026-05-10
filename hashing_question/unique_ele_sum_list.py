
lst = [1, 2, 3, 2] # result => 4

# lst = [1, 1, 1, 1] # result => 0
def unique_ele_sum(lst:list)->int | dict:
    d = {}
    count = 0
    for e in lst:
        if e in d.keys():
            d[e] += 1
        else:
            d[e] = 1

    for key, val in d.items():
        if val == 1:
            count += key

    return count  
  
print(unique_ele_sum(lst))
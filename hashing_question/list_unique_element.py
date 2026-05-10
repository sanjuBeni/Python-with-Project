
lst = [1, 5, 6, 4, 6, 7, 1, 2, 5, 1, 1, 2, 2, 2]

def find_unique_element(lst:list)->int | dict | list:
    if not lst:
        return 0, []
    
    # If say using set then
    # return list(set(lst))
    
    # If not using set, this approch is well
    d = {}
    for e in lst:
        d[e]  = d.get(e, 0) + 1

    # Unique element in list
    # return list(d.keys())

    # Frequency in element in list
    return d

print(find_unique_element(lst))
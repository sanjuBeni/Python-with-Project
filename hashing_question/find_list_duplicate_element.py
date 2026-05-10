
lst = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9]

def find_duplicate_element(lst:list[int])->list:
    if not lst:
        return []
    
    d = {}
    for e in lst:
        d[e] = d.get(e, 0) + 1

    d = {key: value for key, value in d.items() if value > 1}
    return list(d.keys())

print(find_duplicate_element(lst))
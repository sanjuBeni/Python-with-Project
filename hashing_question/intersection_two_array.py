
a = [1, 2, 2, 1, 4, 5]
b = [2, 2, 3, 4, 5, 6, 6, 7, 7, 8]

def xyz(lst1:list, lst2:list)->list|dict:
    if not lst1 or not lst2:
        return []
    
    d = {}
    for e in lst1:
        d[e] = d.get(e, 0) + 1

    u = []
    for e in lst2:
        if d.get(e) and e not in u:
            u.append(e)
    return u

print(xyz(a, b))
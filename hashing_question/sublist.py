
lst = [1, 2, 3]
lst = [4, 5]

def sub_list(lst:list)->list:
    if not lst:
        return []
    
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst) + 1):
            result.append(lst[i:j])

    return result

print(sub_list(lst))
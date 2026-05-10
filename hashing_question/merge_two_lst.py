
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [4,5]

def merge_list(list1:list, list2:list)->list:
    if not list1 or not list2:
        return []
    
    l1 = len(list1)
    l2 = len(list2)
    max_len = l1 if l1 > l2 else l2
    result = []
    for i in range(max_len):
        if i < l1:
            result.append(list1[i])

        if i < l2:
            result.append(list2[i])

    return result

print(merge_list(lst1, lst3))
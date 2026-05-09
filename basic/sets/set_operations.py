set1 = {1,2,3,4,5}
set2 = {3, 4, 5, 6}

def set_operations(set1, set2):
    if not set1 or not set2:
        return set()
    
    print(f"Union: {set1.union(set2)}")
    print(f"Intersection: {set1.intersection(set2)}")
    # print(f"Difference: {set1 - set2}")
    print(f"Difference: {set1.difference(set2)}")

set_operations(set1, set2)


def check_subset_superset(set1, set2):
    
    set1 = set(set1) if not isinstance(set1, set) else set1
    set2 = set(set2) if not isinstance(set2, set) else set2

    is_subset = set1.issubset(set2)     
    is_superset = set1.issuperset(set2)

    if set1 == set2:
        print('Set1 and Set2 are equal')
    elif is_subset:
        print('Set1 is a subset of Set2')
    elif is_superset:
        print('Set1 is a superset of Set2')
    else:
        print('No subset or superset relation')
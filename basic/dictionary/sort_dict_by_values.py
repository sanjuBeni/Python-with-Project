
d = {'a': 3, 'b': 1, 'c': 2}

def sort_dict_by_values(d):
    if not isinstance(d, dict):
        return d
    
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print(sort_dict_by_values(d))
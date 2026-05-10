"""
    Find two string same frequency
"""


s1 = "listen"
s2 = "silent"

def find_string_same_frequency(s1:str, s2:str)->bool|str:
    if not s1 or not s2:
        return ''
    
    d = {}
    for s in s1:
        d[s] = d.get(s, 0) + 1

    for s in s2:
        if not d.get(s):
            return False

    return True

print(find_string_same_frequency(s1, s2))
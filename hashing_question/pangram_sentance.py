"""
    Pangram is contain all character a-z or single.

    if sum of keys are equal to 26 so sentance is pangram
"""

# packmyboxwithfivedozenliquorjugs

sentance = "thequickbrownfoxjumpsoverthelazydog"

def is_pangram(sentance:str)->bool | dict:

    d = {}
    for s in sentance.lower():
        d[s] = d.get(s, 0) + 1

    return len(d.keys()) == 26

    # count = 0
    # for i in range(ord('a'), ord('z') + 1):
    #     if chr(i) in d.keys():
    #         count += 1
    #     else: 
    #         return False 
        
    # return count == 26

print(is_pangram(sentance))
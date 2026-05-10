
"""
    List of people name, list of heights, both list are n length
    people[i] : heights[i]

    find descending order by heights
"""

people = ["Sanjay", "Amit", "Rahul", "Neha"]
heights = [180, 179, 165, 175]

def descending_by_heights(people:list[str], heights:list[int])->list[str]|dict:
    if not people or not heights:
        return []
    
    n = len(people)
    data = {}
    for i in range(n): 
        data[people[i]] = heights[i]

    data = dict(sorted(data.items(), key = lambda x : x[1], reverse=True))
    return list(data.keys())

print(descending_by_heights(people=people, heights=heights))


# def descending_list(lst:list)->list:
#     if not lst:
#         return []
    

        


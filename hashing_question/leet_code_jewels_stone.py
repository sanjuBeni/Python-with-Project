
jewels = 'aA'
stones = 'aAABBB'

# How many jewels in stones

def find_jewels(jewels:str, stones:str)->int:

    count = 0
    for s in stones:
        if s in jewels:
            count += 1

    return count


print(find_jewels(jewels, stones))
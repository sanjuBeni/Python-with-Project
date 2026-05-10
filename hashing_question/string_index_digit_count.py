
num = "1210"

def string_index_digit_count(num:str)->bool:
    d = {}
    for e in num:
        d[e] = d.get(e, 0) + 1

    for i in range(len(num)):
        if d.get(str(i), 0) != int(num[i]):
            return False

    return  True

print(string_index_digit_count(num))
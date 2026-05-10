
# Find first letter of string is twise or not

# letter = 'abccbaacz'
# letter = 'abcdd'
letter = 'abcde'

def first_appeares_twise(letter:str)->str:
    s = ''
    for i in range(len(letter) - 1):
        if letter[i] == letter[i+1]:
            return letter[i]

    return s

print(first_appeares_twise(letter))
    
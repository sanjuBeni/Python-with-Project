# write your code here

"""
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
"""

str1 = input()
str2 = input()

length_str1 = len(str1)
total = 0
for i in str1:
    if i in str2:
        total += 1
if total == length_str1:
    print('Anagram')
else:
    print('Not Anagram')
    

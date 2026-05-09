# write your code here
string = input()

def reverse_string(string):
    str_len = len(string)
    if str_len == 0:
        print(string)
        return
    new_str = ''
    for i in range(len(string) -1, -1, -1):
        new_str += string[i]
    print (new_str);

reverse_string(string)
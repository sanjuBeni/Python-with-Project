
num = int(input())

for i in range(1, num+1):
    s = ''
    for j in range(1, i+1):
        s += str(j)
    print(f"{s}")


# write your code here
num = int(input())
for i in range(num, 0, -1):
    s = ''
    for j in range(1, i+1):
        s += '*'
    print(s)

# write your code here
num = int(input())
for i in range(1, num+1):
    s = ''
    for j in range(1, i+1):
        s += '*'
    print(s)
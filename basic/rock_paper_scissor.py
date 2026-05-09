import random

rock = 1
paper = 2
scissor = 3

my_score = 0
mach_score = 0

while True:
    if my_score == 5 or mach_score == 5:
        break
    mach_num = random.randint(1,3)
    my_num = int(input('Your number: '))

    if my_num == 1 and mach_num == 3:
        print('This round you win...\n')
        my_score += 1
    elif my_num == 2 and mach_num == 1:
        print('This round you win...\n')
        my_score += 1
    elif my_num == 3 and mach_num == 2:
        print('This round you win...\n')
        my_score += 1
    elif my_num == mach_num:
        print('This round tie...\n')
    else:
        print('This round machine win...\n')
        mach_score += 1

if mach_score == 5:
    print('Machine win this game...')
else:
    print('You win this game...')
import random

rand_num = random.randint(1, 100)

tried = 0
while True:
    my_num = int(input('Guess your number: '))
    tried += 1
    if my_num == rand_num:
        print(f'You guess right number, and you tried {tried} time.')
        break
    elif my_num > rand_num:
        print(f"You guess high value, try with lower")
    else:
        print("You guess low value, try with high")
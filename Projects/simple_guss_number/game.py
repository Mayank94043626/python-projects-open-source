from random import randint

guss_count = 0
pc = randint(1, 100)

while (ask := int(input('num from 1 to 100: '))) != pc:
    guss_count += 1
    
    if ask > pc:
        print('your guss is bigger')
    
    elif ask < pc:
        print('your guss is smaller')
    
    ask

print(f'good job! the correct answer is {pc}.\nguss count: {guss_count}')

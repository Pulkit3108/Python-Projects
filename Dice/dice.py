import random
x=input('Press Y to roll the Dice..')
while(x=='Y'or x=='y'):
    n=random.randint(1,6)
    if(n==1):
        print('|-----|')
        print('|--o--|')
        print('|-----|')
    elif(n==2):
        print('|o----|')
        print('|-----|')
        print('|----o|')
    elif(n==3):
        print('|o----|')
        print('|--o--|')
        print('|----o|')
    elif(n==4):
        print('|o---o|')
        print('|-----|')
        print('|o---o|')
    elif(n==5):
        print('|o---o|')
        print('|--o--|')
        print('|o---o|')
    elif(n==6):
        print('|o---o|')
        print('|o---o|')
        print('|o---o|')
    x=input('Press Y to roll the Dice Again..')
    print('Press N to Exit')

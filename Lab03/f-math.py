from random import randint,choice
from eval import calc

x = randint(1, 10)
y = randint(1, 10)

op = choice(['+','-','*','/'])

res = calc(x, y, op)

err=randint(-1, 1)

display_res = res + err
print('*'* 10)
print('{} {} {} = {}'.format(x, op,y, display_res))

ans =input("(Y/N)")

if err == 0 :
    print("Yay")

elif err == 1 :
    print() 








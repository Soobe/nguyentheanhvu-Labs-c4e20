from random import *
from eval import calc

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 10)
    y = randint(1, 10)
    op =choice(['+','-','*','/'])
    res = calc(x ,y, op)

    err = randint(-1, 1)  
    display_res = res + err

    return [x ,y, op, display_res]


def check_answer(x, y, op, result, user_choice):
    # user_choice :True or False
    true_res = calc(x,y,op)
    if true_res == result:
        return user_choice
    else:
        if user_choice :
            return False
        else:
            return True        

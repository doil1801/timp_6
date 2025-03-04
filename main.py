from random import random

n = 6

def func1(f1, f2):
    if (f1 - n)**2/(4*n**2) + (f2 - n)**2/(n**2) <= 1:
        return True
    else:
        return False
    
def func2(f1, f2):
    if n/2 <= f1 <= 3*n:
        return True
    else:
        return False
    
def func3(f1, f2):
    if n/2 <= f2 <= 2*n:
        return True
    else:
        return False
    
l_x = []
l_y = []
while True:
    gen_x = 3 + random()*(18 - 3)
    gen_y = 3 + random()*(12 - 3)
    if func1(gen_x, gen_y) and func2(gen_x, gen_y) and func3(gen_x, gen_y):
        l_x.append(gen_x)
        l_y.append(gen_y)
        if len(l_x) == 200:
            break

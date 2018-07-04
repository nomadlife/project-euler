# Q045 Triangular, pentagonal, and hexagonal
def is_pentagonal(num):
    sol1 = 1/6 + (1+24*num)**0.5/6
    sol2 = 1/6 - (1+24*num)**0.5/6
    if sol1 > 0 and sol1 == int(sol1):
        return True
    elif sol2 > 0 and sol2 == int(sol2):
        return True
    return False

def is_hexagonal(num):
    sol1 = 1/4 + (1+8*num)**0.5/4
    sol2 = 1/4 - (1+8*num)**0.5/4
    if sol1 > 0 and sol1 == int(sol1):
        return True
    elif sol2 > 0 and sol2 == int(sol2):
        return True
    return False
    
for i in range(1,100000):
    t = i*(i+1)/2
    if is_pentagonal(t) and is_hexagonal(t):
        print(t)
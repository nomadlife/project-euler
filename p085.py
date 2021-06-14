print("hello p85.")
def rec(row,col):
    total=0
    for r in range(row):
        for c in range(col):
            total += (row-r)*(col-c)
    return total

margin = 100
for r in range(1500):
    for c in range(1500):
        res = rec(r,c)
        if res > 2000000-margin and res < 2000000+margin:
            print(r,c,res, r*c)
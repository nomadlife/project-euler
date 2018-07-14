# Q043 Sub-string divisibility
# recursion - list reverse, return summ
def ispan(string):
    if all(string.count(x)==1 for x in string):
        return True
    return False

def func(level=6,string=''):
    total=0
    if level==6:
        for j in lists[level]:
            total+=func(5,j)
        return total
    elif level<0 :
        for i in '0123456789':
            if ispan(i+string):
                total+=int(i+string)
        return total
    for i in lists[level]:
        if string[:2] == i[1:] :
            newstr=str(i[0]+string)
            if ispan(newstr):
                total+=func(level-1,newstr)
    return total

lists=[[str(i*j).zfill(3) for i in range(1,500) if i*j<1000] for j in [2,3,5,7,11,13,17]]        
func()
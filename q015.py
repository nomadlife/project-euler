# Q015 Lattice paths
# How many such routes are there through a 20×20 grid?

def grid(r,c):
    if c==0 or r==0:
        return 1
    elif r==1:
        return c+1
    elif c==1:
        return r+1
    else:
        return grid(r,c-1)+grid(r-1,c)

i=0;dim=20;total=0
while i<=dim:
    total = total + grid(i,dim-i)**2
    i+=1

print(total)

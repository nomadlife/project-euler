# Q015 Lattice paths
# How many such routes are there through a 20×20 grid?

def grid(r,c):
    if c==0 or r==0:
        return 1
    elif r==1:
        return c+1
    elif c==1:
        return r+1
    elif (r,c) in cache:
        return cache[r,c]
    else:
        cache[r,c]=grid(r,c-1)+grid(r-1,c)
        return cache[r,c]

cache={}
grid(20,20)
print(cache[20,20])

# Q015 Lattice paths
# How many such routes are there through a 20×20 grid?

def grid(r,c):
    if r==1 or c==1:
        return c+r
    if (r,c) not in cache:
        cache[r,c] = grid(r,c-1) + grid(r-1,c)
    return cache[r,c]

cache={}
grid(20,20)

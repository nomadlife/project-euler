#Q024 Lexicographic permutations, find 1Mth permutation.

def factorial(n):
    for i in range(1,n):
        n*=i
    return n

def permutation(n,i=0):
    move=0
    step = factorial(9-i)
    while n>step:
        n-=step
        move+=1
    result.insert(i,result.pop(i+move))
    if n is not 1:
        permutation(n,i+1)
        
result=list(range(10))
permutation(1000000)
result

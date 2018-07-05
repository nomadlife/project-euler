# p052 Permuted multiples
n=1
while True:
    if set(str(n))==set(str(n*2))==set(str(n*3))==set(str(n*4))==set(str(n*5))==set(str(n*6)):
        print(n)
        break
    n+=1
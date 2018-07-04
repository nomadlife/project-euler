# Q047 Distinct primes factors
from sympy.ntheory import primefactors

ppp=0; pp=0; previous=0; current=0
for i in range(1,1000000):
    ppp,pp, previous, current = pp,previous, current, len(primefactors(i))
    #print("loop:",i,ppp, pp, previous,current)
    if ppp == pp == previous == current == 4:
        print("answer:",i-3)
        break
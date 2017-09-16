a=1;b=1;total=0
while b<=4000000 :
    print(b,end=', ')
    if b%2==0:
        total = total + b
    print(total)
    a,b = b,a+b

# Q028 Number spiral diagonals

n=1001;total=0
for i in range(1,n+1,2):
    value=pow(i,2)
    if i>1:
        total=total+value*4-(i-1)*6
    else:
        total+=i
print(total)

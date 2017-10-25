# Q030 Number spiral diagonals

total=0
for i in range(2,1000000):
    string=str(i)
    value=0
    for j in string:
        value+=pow(int(j),5)
    if i == value:
        print(i)
        total+=i
print(total)

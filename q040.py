# Q040 Champernowne's constant
i=1;string=''
while len(string)<1000000: 
    string += str(i)
    i+=1
total=1
for i in range(7):
    digit=pow(10,i)
    print(digit,string[digit-1])
    total+=int(string[digit-1])*digit
print(total)
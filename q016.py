# Q016 Power digit sum
# What is the sum of the digits of the number 21000?

string=str(2**1000)
i=0
total=0
for i in string:
    total=total+int(i)

print(total)

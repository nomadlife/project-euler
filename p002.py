# Q002 Even Fibonacci numbers
# find the sum of the even-valued terms until 4M

a = 1
b = 1
total = 0
while b <= 4000000:
    if b % 2 == 0:
        total = total + b
    a, b = b, a+b
print(total)

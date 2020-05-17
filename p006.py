# Q006 Sum square difference
# Find the difference between
# the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

total = 0
totalsq = 0
for i in range(1, 101):
    totalsq = totalsq + i**2
    total = total + i

print(totalsq, total, total**2)
print(total**2-totalsq)

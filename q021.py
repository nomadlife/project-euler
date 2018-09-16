# Q021 Amicable numbers
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# Evaluate the sum of all the amicable numbers under 10000.

def divisors(n):
    i=2;total={1}
    while i<=n**0.5:
        if n%i==0:
            total.add(i)
            total.add(n/i)
        i+=1
    return sum(total)

total=0
for i in range(1,10000):
    value = divisors(i)
    if i != value and divisors(value) == i:
        total+=i
print(total)

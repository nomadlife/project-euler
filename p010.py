# Q010 Summation of primes < 2M


def is_prime(num):
    if num == 1:
        return False
    loop = num**0.5
    i = 2
    while i <= loop:
        if num % i == 0:
            return False
        i += 1
    return True


total = 0
i = 1
while i < 2000000:
    if is_prime(i):
        total += i
    i += 1
print(total)

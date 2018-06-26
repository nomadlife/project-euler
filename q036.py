# Q036 Double-base palindromes, ~1M, z8350, 2.5s
total = 0
for i in range(1,1000000):
    string=str(i)
    if string==string[::-1]:
        binary=bin(i)[2:]
        if binary==binary[::-1]:
            total+=i
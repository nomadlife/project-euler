# Q042 Coded triangle numbers

trinum=[n*(n+1)/2 for n in range(20)]
print(sum([1 for x in words if sum([ord(i)-64 for i in x]) in trinum]))
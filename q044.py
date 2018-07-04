# p044 Pentagon numbers
tri = set(i*(3*i-1)/2 for i in range(1,3000))

for i in range(1,3000):
    for j in range(i+1,3000):
        p1 = i*(3*i-1)/2
        p2 = j*(3*j-1)/2
        if p1+p2 in tri and p2-p1 in tri:
            print(i,j,p1,p2,"both pentagonal, diff is ",p2-p1)
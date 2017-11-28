# 1000000까지 카운트

def is_prime(number):
    i=2
    while i <= number**0.5:
        if number % i == 0:
            return False
        i+=1
    return True

count=0
for i in range(2,1000000):
    if is_prime(i):
        #print(i,"is prime",end=",")
        string = str(i)
        is_circular_prime = True
        m=len(string)
        for j in range(1,m):
            string_new = string[j:]+string[:j]
            if not is_prime(int(string_new)):
                is_circular_prime = False
        if is_circular_prime:
            #print(i,"is circular prime")
            count+=1
print(count)

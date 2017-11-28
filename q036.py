import time
start_time = time.time()

def is_palindrome(string):
    string2=string[::-1]
    if string2 == string :
        return True
    return False

total = 0
count = 0
for i in range(1,1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        print(i,bin(i)[2:])
        total+=i
        count+=1
print(total,count)
print("calculation time:", time.time()-start_time)

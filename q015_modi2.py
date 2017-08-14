#project-euler q015
#Longest Collatz sequence

# #the 141990th person to have solved this problem.
#more faster 

import time
start_time = time.time()

def grid(r,c):
    if c==0 or r==0:
        return 1
    elif r==1:
        return c+1
    elif c==1:
        return r+1
    else:
        return grid(r,c-1)+grid(r-1,c)

i=0;dim=20;total=0
while i<=dim:
    total = total + grid(i,dim-i)**2
    i+=1

print(total)


print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))

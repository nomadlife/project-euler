#project-euler q015
#Lattice paths

# #the 141990th person to have solved this problem.
#running time is 1414 sec @3205U, too much slow.

import time
start_time = time.time()

def combination(n1,n2):
    if n2==0:
        return 1
    elif n2==1:
        return n1
    elif n1==n2*2:
        return combination(n1-1,n2-1)*2
    else:
        return combination(n1-1,n2)+combination(n1-1,n2-1)

print(combination(40,20))

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))

#project-euler q017
#Number letter counts

#

import time
start_time = time.time()
filename = 'q017_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string =''
for line in lines:
    print(line.rstrip())
    print(len(line.rstrip()))

i=0
while i<=1000:

    print(lines[i])
    i+=1

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))

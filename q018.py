#project-euler q017
#Number letter counts

# the 116033rd person to have solved this problem.

import time
start_time = time.time()

filename = 'q018_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

'''
i=0;string_i='';length_i=0;total_length=0
while i<1000:
	print("loop:",i,end='')
	string_i=make_string(i)
	print(" string_i:",string_i,end='')
	length_i=len(string_i)
	print(" length_i:",length_i,end='')
	total_length=total_length+length_i
	print(" total_length:",total_length)
	i += 1
print("total_length :",total_length)
'''

print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))

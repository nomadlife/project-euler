#project-euler q017
#Number letter counts

#
'''
import time
start_time = time.time()
'''

filename = 'q017_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

"""
pi_string =''
for line in lines:
    print(line.rstrip())
    print(len(line.rstrip()))
"""

i=0;string_i='';total_length=0
while i<100:
    print("loop:",i,end='')
    if i>20 and i<100:
        string_i = lines[int(str(i)[0])+17].rstrip()
        if int(str(i)[1]) != 0:
            string_i = string_i + lines[int(str(i)[1])-1].rstrip()
        print(" string_i :", string_i, end = '')
    elif i!=0 and i<=20:
        string_i = lines[i-1].rstrip()
        print(" string_i :", string_i, end = '')
    length_string = len(string_i)
    print(" length_string :", length_string, end = '')
    total_length += length_string
    print(" total_length", total_length)
    i += 1

'''
print("***test***")
print("loop:",i,lines[i].rstrip(),end='')
print(" ",len(lines[i]),"",end='')
total=total+i
print(total)


print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
'''

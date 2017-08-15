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

def make_string(number,total_string=''):
	#print(" number",number,end ='')
	string=str(number)
	length=len(string)
	if length==3:
		total_string=lines[int(string[0])-1].rstrip()+"hundred"
		#print(" total_string:",total_string,end='')
		number = number - int(string[0]) * 100
		if number==0:
			return total_string
		total_string=make_string(number,total_string+"and")
	elif number<100 and number > 20:
		total_string=total_string+lines[int(string[0])+17].rstrip()
		#print(" total_string:",total_string,end='')
		number=number-int(string[0])*10
		total_string=make_string(number,total_string)
	elif number != 0 and number <= 20:
		total_string = total_string+lines[number-1].rstrip()
		#print(" total_string:",total_string,end='')
	#print(total_string)
	return total_string

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
print("***test***")
print("loop:",i,lines[i].rstrip(),end='')
print(" ",len(lines[i]),"",end='')
total=total+i
print(total)


print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))
'''

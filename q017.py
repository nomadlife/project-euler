# Q017 Number letter counts
# numbers 1 to 5 : one, two, three, four, five,
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total
# how many letters would be used in numbers from 1 to 1000?


filename = 'q017_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

def make_string(number,string=''):
	charNum=str(number)
	lenNum=len(charNum)
	if lenNum==3:
		string=lines[int(charNum[0])-1].rstrip()+"hundred"
		number = number - int(charNum[0]) * 100
		if number==0:
			return string
		string=make_string(number,string+"and")
	elif number<100 and number > 20:
		string=string+lines[int(charNum[0])+17].rstrip()
		number=number-int(charNum[0])*10
		string=make_string(number,string)
	elif number != 0 and number <= 20:
		string = string+lines[number-1].rstrip()
	return string

i=1;length_i=0;total_length=0
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
print("add 1000(one thousand,11 letters)",total_length+11)

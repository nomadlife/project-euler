#project-euler q008
#Largest Product in Series

filename = 'q008_data.txt'
with open(filename) as file_object:
	#contents = file_object.read()
	lines = file_object.readlines()

#pi_string =''
for line in lines:
	#pi_string+= line.rstrip()
	print(line)

print(lines[0])

#print(pi_string)
#print(len(pi_string))
#print(pi_string[1000])
#print(int(pi_string[0])*int(pi_string[1]))
#print(contents)

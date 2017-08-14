#project-euler q008
#Largest Product in Series

filename = 'q008_data.txt' 
with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string =''
for line in lines:
	pi_string+= line.rstrip()

i=0;max_product=0
while i<1000:
	j=0;product=1
	while j<13:
		product=product*int(pi_string[i+j])
		j+=1
	if product>max_product:
		max_product=product
	if i+12==999:
		break
	i+=1
		
print("final max_product :",max_product)
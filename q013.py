# q013 Large sum
# Work out the first ten digits of the sum
# of the following one-hundred 50-digit numbers.

filename = 'q013_data.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_sum=0
for line in lines:
    pi_sum+= int(line.rstrip())

print(pi_sum)
print(str(pi_sum)[0:10])

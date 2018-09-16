# q013 Large sum
# Work out the first ten digits of the sum
# of the following one-hundred 50-digit numbers.

with open('q013_data.txt') as data:
	total = sum(int(i) for i in data.read().split())

str(total)[:10]

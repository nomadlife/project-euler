#project-euler q018
#Maximum path sum 1
# the 112037th person to have solved this problem.

import time
start_time = time.time()

import q018_init
import q018_functions as q018


q018_init.load_array()
print(numbers)

print(q018.biggest_sum())
print(q018.biggest_path())


print("start_time", start_time)
print("--- %s seconds ---" %(time.time() - start_time))

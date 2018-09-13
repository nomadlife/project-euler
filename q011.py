# Q011 Largest Product in grid 20x20
# greatest product of four adjacent numbers in the same direction

import numpy as np
with open('q011_data.txt') as f:
    numbers = np.array(f.read().split()).astype(int).reshape(20,20)

result=[]
for i in range(20):
    for j in range(20):
        arr = numbers[i:i+4,j:j+4]
        result.append(max(\
            arr[0].prod(),
            arr[:,0].prod(),
            arr.diagonal().prod(),
            arr[::-1].diagonal().prod()))
max(result)

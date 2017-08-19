import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print(sys.argv[1])

loop=2000000
if len(sys.argv)==2:
    print ("sys.argv==2")
    loop=int(sys.argv[1])
if int(sys.argv[1])==int:
    print ("sys.argv is int")
else:
    print ("sys.argv is not int")

print("loop=",loop)

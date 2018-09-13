# Q019 Counting Sundays
# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
total=0
count=0
for y in range(1900,2001):
    for m in range(12):
        monthday=daylist[m]
        if y%4==0 and m==1: 
            monthday+=1
        for d in range(monthday):
            if y>1900 and d==0 and total%7==6:
                count+=1
            total+=1

print(count)

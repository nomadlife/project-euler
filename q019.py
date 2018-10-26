# Q019 Counting Sundays
# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

totalDay = 0
sundayCount = 0
for y in range(1900,2001):
    for m in [31,28,31,30,31,30,31,31,30,31,30,31]:
        if y % 4 == 0 and m == 28: 
            m += 1
        for d in range(m):
            if y > 1900 and d == 0 and totalDay % 7 == 6:
                sundayCount += 1
            totalDay += 1

sundayCount

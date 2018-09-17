# p054 Poker hands
with open('p054_poker.txt') as data:
    games = [''.join(i.split()) for i in data.readlines()]

def grader(count):
    pair = count[:14]
    suit = count[14:18]
    rank=[0]*9
    if '1' in pair:        rank[8] = pair.rindex('1')
    if pair.count('2')==1: rank[7] = pair.index('2')
    if pair.count('2')==2: rank[6] = pair.rindex('2')
    if '3' in pair:        rank[5] = pair.index('3')
    if '11111' in pair:    rank[4] = rank[8]
    if '5' in suit:        rank[3] = rank[8]   
    if rank[7] != 0 and rank[5] != 0 : rank[2] = rank[5]    
    if '4' in pair:                    rank[1] = pair.index('4')
    if rank[4] != 0 and rank[3] != 0 : rank[0] = rank[4]    
    return rank

def counter(g):
    c='0' 
    for i in '23456789TJQKACSHD':
        c+=str(g.count(i))
    return c

p1count=0
for g in games:
    r1 = grader(counter(g[:10]))
    r2 = grader(counter(g[10:20]))
    if r1 > r2:
        p1count+=1
print(p1count)

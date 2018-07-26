# p054 Poker hands
with open('p054_poker.txt') as data:
    games = [''.join(i.split()) for i in data.readlines()]

def winner(r1,r2):
    for i in range(8,-1,-1):
        if r1[i]>r2[i]:
            return 'p1'
        elif r1[i]<r2[i]:
            return 'p2'
    return 'tie'

def grader(count):
    pair = count[:13]
    suit = count[13:17]
    rank=[0]*9
    if '1' in pair:        rank[0] = pair.rindex('1')
    if pair.count('2')==1: rank[1] = pair.index('2')
    if pair.count('2')==2: rank[2] = pair.rindex('2')
    if '3' in pair:        rank[3] = pair.index('3')
    if '11111' in pair:    rank[4] = rank[0]
    if '5' in suit:        rank[5] = rank[0]   
    if rank[1] != 0 and rank[3] != 0 : rank[6] = rank[3]    
    if '4' in pair:                    rank[7] = pair.index('4')
    if rank[4] != 0 and rank[5] != 0 : rank[8] = rank[4]    
    return rank

def counter(g):
    c=''
    for i in '23456789TJQKACSHD':
        c+=str(g.count(i))
    return c

p1count=0
for g in games:
    g1=grader(counter(g[:10]))
    g2=grader(counter(g[10:20]))
    if winner(g1,g2)=='p1':
        p1count+=1
print(p1count)
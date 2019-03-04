# p054 Poker hands
with open('p054_poker.txt') as data:
    games = [''.join(i.split()) for i in data.readlines()]

def grader(cards):
    no_of_cards = '00'+''.join([str(cards.count(i)) for i in '23456789TJQKACSHD'])
    number_part = count
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

p1win = 0
for hand in games:
    if grader(counter(hand[:10])) > grader(counter(hand[10:20])):
        p1win+=1
print(p1win)

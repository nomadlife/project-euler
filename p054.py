# p054 Poker hands
with open('p054_poker.txt') as data:
    games = [i.split() for i in data.readlines()]

def whowin(results):
    keywords='High,One,Two,Three,Straight,Flush,Full House,Four,Straight Flush,Royal Flush'
    orders = keywords.split(',')[::-1]
    for key in orders:
        if results[0][key] > results[1][key] :
            return 'player 1 win'
        elif results[0][key] < results[1][key] :
            return 'player 2 win'
    return 'no decision'

def evaluate(pair,suit):
    keyword='High,One,Two,Three,Straight,Flush,Full House,Four,Straight Flush,Royal Flush'
    ranks=dict(zip(keyword.split(','),[0]*10))
    if 1 in pair:
        ranks['High'] = 12-pair[::-1].index(1)
    if pair.count(2)==1:
        ranks['One'] = pair.index(2)
    if pair.count(2)==2:
        ranks['Two'] = pair.index(2,pair.index(2)+1)
    if 3 in pair:
        ranks['Three'] = pair.index(3)
    if 4 in pair:
        ranks['Four'] = pair.index(4)
    if 5 in suit:
        ranks['Flush'] = ranks['High']
    if '11111' in ''.join([str(x) for x in pair]):
        ranks['Straight'] = ranks['High']
    if ranks['One'] != 0 and ranks['Three'] != 0 :
        ranks['Full House'] = ranks['Three']
    if ranks['Straight'] != 0 and ranks['Flush'] != 0:
        ranks['Straight Flush'] = ranks['Straight']
    return ranks
    
def count(cards):
    pair=[0]*13
    suit=[0]*4
    for card in cards:
        for i,v in enumerate('23456789TJQKA'):
            if card[0] == v:
                pair[i]+=1
        for i,v in enumerate('CSHD'):
            if card[1] == v:
                suit[i]+=1
    return evaluate(pair,suit)

count_win=0
for game in games:
    results=[]
    results.append(count(game[0:5]))
    results.append(count(game[5:10]))
    decision = whowin(results)
    if decision == 'player 1 win':
        count_win+=1
print(count_win)
import random
from itertools import combinations

#chaptr = ['Jackline', 'Linet', 'Carolyne', 'Rodgers', 'Lwanga', 'Kipkorir', 'Chris', 'Rohi', 'Aseta', 'Kiinga', 'Cyril', 'Jesse', 'Nobella', 'Nigel']
lst = [1,2,3,4,5,6,7,8,9,10]
comb = list(combinations(lst, 2))
weeks = len(comb)/(len(lst)/2)

print(len(comb),len(lst)/2, weeks)

matches = list()

#Create weekly peer matches
while len(matches) < len(lst)//2:
    match = random.choice(comb)
    matches.append(match)
    comb.remove(match)
    print(len(comb))
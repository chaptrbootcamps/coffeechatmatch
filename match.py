import random
from itertools import combinations


def creatematches(lst, match_size):
    
    matches = list()
    rem_lst = list()

    #Execute this if group size is not divisible by match size
    if len(lst)%match_size != 0:
        rem = len(lst)%match_size

        #choose random people who will be added to groups separately
        for i in range(rem):
            indv = random.choice(lst)
            rem_lst.append(indv)
            lst.remove(indv)

    while len(lst) > 0:
        #stipulate the possible combinations and choose a match
        comb = list(combinations(lst, match_size))
        match = list(random.choice(comb))
        matches.append(match)

        #Remove already matched persons from list for next match
        for i in match:
            lst.remove(i)

    #Add the left out individuals into a random matched group
    if len(rem_lst) > 0:
        for i in range(len(rem_lst)):
            matches[i].append(rem_lst[i])

    return matches


##Add created matches to a database (Use databse to avoid future repetition)
def savematches(matches):
    print("Done")


chaptr = ['Jackline', 'Linet', 'Carolyne', 'Rodgers', 'Lwanga', 'Kipkorir', 'Chris', 'Rohi', 'Aseta', 'Kiinga', 'Cyril', 'Jesse', 'Nobella', 'Nigel']
matches = creatematches(chaptr, 2)
print(matches)
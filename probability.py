##total = 0
##ls = [0,0,0,0,0,0]
##for b in range(6):
##    ls[0] = b
##    for c in range(6):
##        ls[1] = c
##        for d in range(6):
##            ls[2] = d
##            for e in range(6):
##                ls[3] = e
##                for f in range(6):
##                    ls[4] = f
##                    for g in range(6):
##                        ls[5] = g
##                        print(ls)
##                        if ls[0] == ls[1]:
##                            total += 1
##                        elif ls[0] == ls[2]:
##                            total += 1
##                        elif ls[0] == ls[3]:
##                            total += 1
##                        elif ls[0] == ls[4]:
##                            total += 1
##                        elif ls[0] == ls[5]:
##                            total += 1
##
##                        elif ls[1] == ls[2]:
##                            total += 1
##                        elif ls[1] == ls[3]:
##                            total += 1
##                        elif ls[1] == ls[4]:
##                            total += 1
##                        elif ls[1] == ls[5]:
##                            total += 1
##
##                        elif ls[2] == ls[3]:
##                            total += 1
##                        elif ls[2] == ls[4]:
##                            total += 1
##                        elif ls[2] == ls[5]:
##                            total += 1
##
##                        elif ls[3] == ls[4]:
##                            total += 1
##                        elif ls[3] == ls[5]:
##                            total += 1
##
##                        elif ls[4] == ls[5]:
##                            total += 1
##    ls = [0,0,0,0,0,0]
##print(total/46656)


dice = [3,5,2,2,2,1]

##def check_dupliates(dice):
##    for i in range(len(dice)):
##        for j in range(len(dice)):
##            if i == j:
##                continue
##            if dice[i] == dice[j]:
##                return dice[i]
##    return -1
##def check_dupliates(dice):
##    return len(set(dice)) != len(dice)
##def get_duplicate(dice):
##
##seen = {}
##dupes = []
##
##for x in dice:
##    if x not in seen:
##        seen[x] = 1
##    else:
##        if seen[x] == 1:
##            dupes.append(x)
##        seen[x] += 1
##print(dupes)
seen = []
for i in dice:
    if i in seen:
        print(i)
    else:
        seen.append(i)
##print(set([x for x in dice if dice.count(x) > 1]))
##print(check_dupliates(dice))


    

import re

with open("puzzle2_input.txt", "r") as x:
    Count = 1000
    keysAndPwds = [re.split(':| ', line) for line in x]
    keyRange = [i[0].split("-") for i in keysAndPwds]
    keys = [i[1] for i in keysAndPwds]
    pswds = [i[3] for i in keysAndPwds]
    for i in range(len(keysAndPwds)):
        if keys[i] not in pswds[i]:
            print(keys[i])
            Count -= 1
            print(keys[i], pswds[i])
        elif pswds[i].count(keys[i]) not in range(int(keyRange[i][0]), (int(keyRange[i][1])+1)): 
            Count -= 1
    print(Count)

with open("puzzle2_input.txt") as x:
    d = []
    dPlus = []
    Count = 1000
    for line in x:
        d.append(line.split(": "))
    for i in d:
        dPlus.append(i[0].split("-"))
    for i in range(len(d)):
        if dPlus[i][-1][-1] in d[i][1][int(dPlus[i][0])-1]:
            if dPlus[i][-1][-1] in d[i][1][int(dPlus[i][1][:-2])-1]:
                Count -= 1
        if dPlus[i][-1][-1] not in d[i][1][int(dPlus[i][0])-1]:
            if dPlus[i][-1][-1] not in d[i][1][int(dPlus[i][1][:-2])-1]:
                Count -= 1
    print(Count)
    

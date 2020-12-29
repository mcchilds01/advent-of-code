import re

with open("puzzle2_input.txt", "r") as x:
    Count = 1000
    keysAndPwds = [re.split(':| ', line) for line in x]
    keyRange = [i[0].split("-") for i in keysAndPwds]
    keys = [i[1] for i in keysAndPwds]
    pswds = [i[3] for i in keysAndPwds]
    for i in range(len(keysAndPwds)):
        if keys[i] not in pswds[i]:
            Count -= 1
        elif pswds[i].count(keys[i]) not in range(int(keyRange[i][0]), (int(keyRange[i][1])+1)): 
            Count -= 1
    print(Count)

with open("puzzle2_input.txt") as x:
    Count = 1000
    keysAndPwds = [re.split(':| ', line) for line in x]
    keyRange = [i[0].split("-") for i in keysAndPwds]
    keys = [i[1] for i in keysAndPwds]
    pswds = [i[3] for i in keysAndPwds]
    for i in range(len(keysAndPwds)):
        if keys[i] in pswds[i][int(keyRange[i][0])-1]:
            if keys[i] in pswds[i][int(keyRange[i][1])-1]:
                Count -= 1
        if keys[i] not in pswds[i][int(keyRange[i][0])-1]:
            if keys[i] not in pswds[i][int(keyRange[i][1])-1]:
                Count -= 1
    print(Count)

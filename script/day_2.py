with open("puzzle2_input.txt", "r") as x:
    d = []
    dPlus = []
    Count = 1000
    for line in x:
        d.append(line.split(": "))
    for i in d:
        dPlus.append(i[0].split("-"))
    for i in range(len(d)):
        if dPlus[i][-1][-1] not in d[i][1]:
            Count -= 1
        elif d[i][1].count(dPlus[i][-1][-1]) not in range(int(dPlus[i][0]), int(dPlus[i][1][:-2])+1):
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
    
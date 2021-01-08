with open("puzzle10_input.txt") as f:
    rows = [int(i.strip()) for i in f]

rows.append(0)
adapters = sorted(rows)

def getDiffs(adapters_list: list) -> int:
    diffs = [adapters_list[i]-adapters_list[i-1] for i in range(1, len(adapters_list))]
    return (diffs.count(1))*(diffs.count(3)+1)

print("Part I:", getDiffs(adapters))

memo = {}
counter = 0
def getPossibleRoutes(adapters_list: list, i: int) -> int:
    global counter
    if i == len(adapters_list)-1:
        return 1
    if i in memo:
        return memo[i]
    for j in range(1, 4):
        if i+j <len(adapters_list) and adapters_list[i+j] - adapters_list[i] <= 3:
            counter += getPossibleRoutes(adapters_list, i+j)
    memo[i] = counter
    return counter

print("Part II:", getPossibleRoutes(adapters, 0))
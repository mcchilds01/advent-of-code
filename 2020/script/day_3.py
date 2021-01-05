def moveToboggan(start_point, right, down):
    start_point[0] += down
    start_point[1] += right
    return start_point

def getTrees(rows, right, down): 
    rowMaxIndex = len(rows[0])-1
    start = [0, 0]
    count = 0    
    for row in range(0, len(rows)):
        if start[1] > rowMaxIndex:
            start[1] -= rowMaxIndex+1
        if start[0] > len(rows):
            break
        if rows[start[0]][start[1]] == '#':
            count += 1
        moveToboggan(start, right, down)
    return count

with open('puzzle3_input.txt') as p:
    rows = [row.strip('\n') for row in p]

trees1_1 = getTrees(rows, 1, 1)
trees3_1 = getTrees(rows, 3, 1)
trees5_1 = getTrees(rows, 5, 1)
trees7_1 = getTrees(rows, 7, 1)
trees1_2 = getTrees(rows, 1, 2)

treesTotal = trees1_1*trees3_1*trees5_1*trees7_1*trees1_2
print(treesTotal)

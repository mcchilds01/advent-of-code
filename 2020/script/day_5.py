def findRow(boarding_pass: str, boarding_max: int, boarding_min: int) -> int:
    rowMax = boarding_max
    rowMin = boarding_min
    rowRange = [i for i in range(rowMin, rowMax)]
    for i in range(0, 6):
        if boarding_pass[i] == 'F':
            rowMax = rowRange[int((rowMax-rowMin)/2)]
            rowRange = [i for i in range(rowMin, rowMax)]
        else: 
            rowMin = rowRange[int((rowMax-rowMin)/2)]
            rowRange = [i for i in range(rowMin, rowMax)]
    if boarding_pass[6] == 'F': return rowRange[0]
    else: return rowRange[1]

def findColumn(boarding_pass: str, boarding_max: int, boarding_min: int) -> int:
    rowMax = boarding_max+1
    rowMin = boarding_min
    rowRange = [i for i in range(rowMin, rowMax)]
    for i in range(7, 9):
        if boarding_pass[i] == 'L':
            rowMax = rowRange[int((rowMax-rowMin)/2)]
            rowRange = [i for i in range(rowMin, rowMax)]
        else: 
            rowMin = rowRange[int((rowMax-rowMin)/2)]
            rowRange = [i for i in range(rowMin, rowMax)]
    if boarding_pass[9] == 'R': return rowRange[1]
    else: return rowRange[0]

with open('puzzle5_input.txt') as f:
    boarding_passes = [row.strip() for row in f]

ids = []
for i in range(len(boarding_passes)):
    column = findColumn(boarding_passes[i], 7, 0)
    row = findRow(boarding_passes[i], 128, 0)
    ids.append((row*8)+column)
print(max(ids))

ids.sort()
for i in range(1, len(ids)):
    if ids[i] - ids[i-1] > 1:
        print(ids[i-1] + 1)


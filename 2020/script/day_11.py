with open("puzzle11_input.txt") as f:
    rows = [list(x.strip()) for x in f]

for row in rows:
    row.insert(0, '.')
    row.append('.')

s = ['.' for i in range(len(rows[0]))]
rows.insert(0,s)
rows.append(s)

def getChanges1(rows_list:list):
    x = len(rows_list)
    y = len(rows_list[0])
    new_list = [row[:] for row in rows_list]
    for i in range(1, x):
        for j in range(y):
            if rows_list[i][j]=='L':
                if (rows_list[i-1][j-1:j+2].count('#') + 
                    rows_list[i][j-1:j+2].count('#') + rows_list[i+1][j-1:j+2].count('#'))==0:
                    new_list[i][j] = '#'
            if rows_list[i][j]=='#':
                if (rows_list[i-1][j-1:j+2].count('#') + 
                    rows_list[i][j-1:j+2].count('#') + rows_list[i+1][j-1:j+2].count('#'))>=5:
                    new_list[i][j] = 'L'
    return(new_list)

def getCount(lists):
    counter = 0
    for i in range(len(lists)):
        counter += lists[i].count('#')
    return counter

def getEndState(list_rows: list) -> int:
    list1 = list_rows
    list2 = getChanges1(list1)
    while getCount(list1) != getCount(list2):
        list1 = [row[:] for row in list2]
        list2 = getChanges1(list2)
    print(getCount(list2))

getEndState(rows)

mi = (len(rows)-2)
mj = (len(rows[0])-2)

def increment(rows_list: list, i: int, j: int, original: str) -> str:
    signs = []
    x = int(i)
    y = int(j)  
    while i < mi and rows_list[i+1][j] == '.':
        i += 1
    signs.append(rows_list[i+1][j])
    i=int(x)
    j=int(y)
    while i > 0 and rows_list[i-1][j] == '.':   
        i -= 1
    signs.append(rows_list[i-1][j])
    i=int(x)
    j=int(y)
    while j>1 and rows_list[i][j-1] == '.':
        j -= 1
    signs.append(rows_list[i][j-1])
    i=int(x)
    j=int(y)
    while j < mj and rows_list[i][j+1] == '.':
        j += 1
    signs.append(rows_list[i][j+1])
    i=int(x)
    j=int(y)
    while i > 1 and j > 1 and rows_list[i-1][j-1] == '.':
        i -= 1
        j -= 1
    signs.append(rows_list[i-1][j-1])
    i=int(x)
    j=int(y)
    while i > 1 and j < mj and rows_list[i-1][j+1] == '.':
        i -= 1
        j += 1
    signs.append(rows_list[i-1][j+1])
    i=int(x)
    j=int(y)
    while i < mi and j > 1 and rows_list[i+1][j-1] == '.':      
        i += 1
        j -= 1
    signs.append(rows_list[i+1][j-1])
    i=int(x)
    j=int(y)
    while i < mi and j < mj and rows_list[i+1][j+1] == '.':
            i += 1
            j += 1
    signs.append(rows_list[i+1][j+1])
    if signs.count('#') >= 5:
        return 'L'
    elif signs.count('#') == 0: 
        return '#'
    else: 
        return original 

def getChanges2(rows_list:list):
    x = len(rows_list)
    y = len(rows_list[0])
    new_list = [row[:] for row in rows_list]
    for i in range(x):
        for j in range(y-1):
            if rows_list[i][j]=='L':
                new_list[i][j] = increment(rows_list, i, j, "L")
            if rows_list[i][j]=='#':
                new_list[i][j] = increment(rows_list, i, j, "#")
    return(new_list)

def getEndState2(list_rows: list) -> int:
    list1 = list_rows
    list2 = getChanges2(list1)
    while getCount(list1) != getCount(list2):
        list1 = [row[:] for row in list2]
        list2 = getChanges2(list2)
    print(getCount(list2))

getEndState2(rows)

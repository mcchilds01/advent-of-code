# with open ("test_input_12.txt") as f:
#     directions = [row.strip() for row in f]

with open ("puzzle12_input.txt") as f:
    directions = [row.strip() for row in f]

def getManhattanDist(directions_list: list, main_direction: str) -> int:
    NSEW = ['N', 'E', 'S', 'W']
    main = main_direction
    tally = [0, 0]
    for i in directions_list:
        if i[0] == 'N':
            tally[0] += int(i[1:])
        elif i[0] == 'S':
            tally[0] -= int(i[1:])
        elif i[0] == 'E':
            tally[1] += int(i[1:])
        elif i[0] == 'W':
            tally[1] -= int(i[1:])
        elif i[0] == 'L':
            main = NSEW[NSEW.index(main) - int(int(i[1:])/90)]
        elif i[0] == 'R':
            if NSEW.index(main) + int(int(i[1:])/90) < 3:
                main = NSEW[NSEW.index(main) + int(int(i[1:])/90)]
            else: main = NSEW[int(int(i[1:])/90) - (4 - NSEW.index(main))]
        elif i[0] == 'F':
            new = str(main + i[1:])
            tally[0] += getManhattanDist([new], main)[0]
            tally[1] += getManhattanDist([new], main)[1]
    return tally

distTally = getManhattanDist(directions, "E")
print("Part I:", abs(distTally[0])+abs(distTally[1]))

def getManhattanDist2(directions_list: list, main_directions: list) -> int:
    NSEW = ['N', 'E', 'S', 'W']
    main = main_directions
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    waypoint = [1, 10]
    location = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    for i in directions_list:
        if i[0] in NSEW:
            if i[0] in main:
                waypoint[main.index(i[0])] += int(i[1:])
            else: 
                waypoint[main.index(opposite[i[0]])] -= int(i[1:])
        if i[0] == 'L':
            main[0] = NSEW[NSEW.index(main[0]) - int(int(i[1:])/90)]
            main[1] = NSEW[NSEW.index(main[1]) - int(int(i[1:])/90)]
        elif i[0] == 'R':
            if NSEW.index(main[0]) + int(int(i[1:])/90) < 3:
                main[0] = NSEW[NSEW.index(main[0]) + int(int(i[1:])/90)]
            else: main[0] = NSEW[int(int(i[1:])/90) - (4 - NSEW.index(main[0]))]
            if NSEW.index(main[1]) + int(int(i[1:])/90) < 3:
                main[1] = NSEW[NSEW.index(main[1]) + int(int(i[1:])/90)]
            else: main[1] = NSEW[int(int(i[1:])/90) - (4 - NSEW.index(main[1]))]
        elif i[0] == 'F':
            waypoint
            location[main[0]] += int(i[1:])*waypoint[0]
            location[opposite[main[0]]] -= int(i[1:])*waypoint[0]
            location[main[1]] += int(i[1:])*waypoint[1]
            location[opposite[main[1]]] -= int(i[1:])*waypoint[1]
    total = abs(location[main[0]]) + abs(location[main[1]])
    return total

print("Part II:", getManhattanDist2(directions, ["N", "E"]))
with open("puzzle13_input.txt") as f:
    info = [i.strip() for i in f]

departTime = int(info[0])
options = [int(i.strip()) for i in info[1].split(',') if i != 'x']

def getNextBus(departure_time: int, bus_list: list) -> int: 
    nextBuses = {}
    for i in bus_list:
        time = (departure_time%i)
        timeOver = (i - time)
        nextBuses[timeOver] = i
    bestChoice = min(nextBuses.keys())
    return [nextBuses[bestChoice], bestChoice]

print("Part I:", getNextBus(departTime, options)[0]*getNextBus(departTime, options)[1])

newBuses = [int(i.strip()) if i != 'x' else i.strip() for i in info[1].split(',')]
enum = [[count, value] for count, value in enumerate(newBuses)]
busAndOffset = [i for i in enum if type(i[1]) == int]

def getBusesInAlignment(bus_list: list) -> int:
    time = busAndOffset[0][1]
    step = busAndOffset[0][1] 
    for i in range(len(busAndOffset)-1):
        offset = busAndOffset[i+1][0]
        while (time+offset)%(busAndOffset[i+1][1]) != 0:
            time+=step
        step *= busAndOffset[i+1][1]
    return time

print("Part II:", getBusesInAlignment(busAndOffset))


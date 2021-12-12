with open('input_6.txt', 'r') as f:
	inputs =  [i.split(',') for i in f]

fish = [int(i) for i in inputs[0]]

for i in range(80):
	for j in range(len(fish)):
		if fish[j] == 0:
			fish[j] = 6
			fish.append(8)
		else:
			fish[j] -= 1
print(len(fish))


############################################

fish_2 = [int(i) for i in inputs[0]]
fish_sched = [0]*9 
for i in fish_2:
	fish_sched[i] += 1

days = 256

for i in range(days):
	transition = fish_sched[1:]
	transition.append(fish_sched[0])
	transition[6] += fish_sched[0]
	fish_sched = transition

print(sum(transition)) 
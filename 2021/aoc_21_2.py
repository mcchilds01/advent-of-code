with open('input_2.txt', 'r') as f:
	input=  [i.strip() for i in f]

horizontal = 0
vertical = 0
for i in input:
	if i.split(' ')[0] == 'down':
		vertical += int(i.split(' ')[1])
	elif i.split(' ')[0] == 'up':
		vertical -= int(i.split(' ')[1])
	elif i.split(' ')[0] == 'forward':
		horizontal += int(i.split(' ')[1])

print(horizontal, vertical, (horizontal*vertical))

horizontal = 0
vertical = 0
aim = 0 
for i in input:
	if i.split(' ')[0] == 'down':
		aim += int(i.split(' ')[1])
	elif i.split(' ')[0] == 'up':
		aim -= int(i.split(' ')[1])	
	elif i.split(' ')[0] == 'forward':
		horizontal += int(i.split(' ')[1])
		vertical += (aim*int(i.split(' ')[1]))

print(horizontal, aim, (horizontal*vertical))
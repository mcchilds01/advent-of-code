with open('input_4.txt', 'r') as f:
	inputs =  [i.strip() for i in f]

numbers = [i for i in inputs[0].split(',')]
cards_input = [i.split() for i in inputs[1:] if i != '']
cards_input = [list(cards_input[i:i+5]) for i in range(0, len(cards_input), 5)]

def update(card, number):
	for i in range(len(card)):
		for j in range(len(card[i])):
			if card[i][j] == number:
				card[i][j] = '*'

def check_horizontal(card, number):
	for i in range(len(card)):
		if card[i] == list('*'*len(card[0])):
			return True, i
	return False, 0 

def check_vertical(card, number):
	verts = []
	for j in range(len(card[0])):
		for i in range(len(card)):
			if card[i][j] == '*':
				verts.append('*')
		if len(verts) == len(card):
			return True, j
		verts = []
	return False, 0

def bingo(cards, numbers):
	for number in numbers:
		for card in cards:
			update(card, number)
			horizontal, i = check_horizontal(card, number)
			vertical, j = check_vertical(card, number)
			if horizontal == True :
				print("Found our winner!")
				return card, number
			elif vertical == True:
				print("Found our winner!")
				return card, number

winner, number = bingo(cards_input, numbers)
prize = 0
for i in winner:
	for j in i:
		if j != '*':
			prize+=int(j)
print("Final answer: ", prize * int(number))

##########################################

def lose_bingo(cards, numbers):
	continue_list = []
	for number in numbers:
		for card in cards:
			update(card, number)
			horizontal, i = check_horizontal(card, number)
			vertical, j = check_vertical(card, number)
			if horizontal != True and vertical != True:
				continue_list.append(card)
		if len(continue_list) == 1:
			numbers = numbers[numbers.index(number):]
			for number in numbers: 
				update(card, number)
				horizontal, i = check_horizontal(card, number)
				vertical, j = check_vertical(card, number)
				if horizontal == True or vertical == True:
					print('Squid wins!')
					return continue_list, number
		cards = continue_list
		continue_list = []

last_winner, number = lose_bingo(cards_input, numbers)

prize = 0
for i in last_winner[0]:
	for j in i:
		if j != '*':
			prize+=int(j)
print("Final answer: ", prize * int(number))





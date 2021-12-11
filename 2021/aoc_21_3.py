with open('input_3.txt', 'r') as f:
	input=  [i.strip() for i in f]

# input = ['00100', '11110', '10110', '10111', '10101', '01111', 
# '00111', '11100', '10000', '11001', '00010', '01010']

gamma_dict = {}
for i in input:
	for j in range(len(i)):
		if j not in gamma_dict.keys():
			gamma_dict[j] = {'0': 0, '1': 0}
			if i[j] == "0":
				gamma_dict[j]['0'] = 1
			else: gamma_dict[j]['1'] = 1
		else: gamma_dict[j][i[j]] += 1
gamma = int(''.join([max(i, key=i.get)for i in gamma_dict.values()]), 2)
epsilon = int(''.join([min(i, key=i.get)for i in gamma_dict.values()]), 2)

print(gamma * epsilon)

##############################################################



copy_input_1 = input.copy()
zeroes = []
ones = []
zero = 0
one = 0
for i in range(len(copy_input_1[0])):
	for j in copy_input_1:
		if j[i] == '1':
			ones.append(j)
			one += 1
		else: 
			zeroes.append(j)
			zero += 1
	if zero == one or max(zero, one) == one:
		if len(ones) == 1:
			oxygen = int(ones[0], 2)
			print("Answer: ", int(ones[0], 2))
			break
		zeroes = []
		copy_input_1 = ones
		ones = []
		zero = 0
		one = 0
	elif max(zero, one) == zero:
		if len(zeroes) == 1: 
			oxygen = int(zeroes[0], 2)
			print("Answer: ", int(zeroes[0], 2))
			break
		ones = []
		copy_input_1 = zeroes
		zeroes = []
		zero = 0
		one = 0

copy_input_2 = input.copy()

zeroes = []
ones = []
zero = 0
one = 0
for i in range(len(copy_input_2[0])):
	for j in copy_input_2:
		if j[i] == '1':
			ones.append(j)
			one += 1
		else: 
			zeroes.append(j)
			zero += 1
	if zero == one or min(zero, one) == zero:
		if len(zeroes) == 1:
			co2 = int(zeroes[0], 2)
			print("Answer: ", int(zeroes[0], 2))
			break
		ones = []
		copy_input_2 = zeroes
		zeroes = []
		zero = 0
		one = 0
	elif min(zero, one) == one: 
		if len(ones) == 1:
			co2 = int(ones[0], 2)
			print("Answer: ", int(ones[0], 2))
			break
		zeroes = []
		copy_input_2 = ones
		ones = []
		zero = 0
		one = 0

print("Final answer: ", co2*oxygen)

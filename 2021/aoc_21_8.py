with open('input_8.txt', 'r') as f:
	inputs =  {i.split('|')[0].strip(): i.split('|')[1].strip().split() for i in f}

count_of_uniques = [1 for i in inputs.values() for j in i if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) ==7]

# print(sum(count_of_uniques))

###################################################


def map_display(input_signal):
	right = []
	top = []
	four_arm = []
	for i in sorted(input_signal.split(), key=len):
		if len(i) == 2:
			right = [j for j in i]
		elif len(i) == 3:
			for j in i:
				if j not in right:
					top = [j]
		elif len(i) == 4:
			for j in i:
				if j not in right:
					four_arm.append(j)
	return right, top, four_arm

			
def get_sequences(inputs):
	sequences = []
	for signal, output in inputs.items():
		right, top, four_arm = map_display(signal)
		digits = []
		for j in output:
			if len(j) == 2:
				digits.append('1')
			elif len(j) == 3: 
				digits.append('7')
			elif len(j) == 4:
				digits.append('4')
			elif len(j) == 7:
				digits.append('8')
			elif len(j) == 5:
				if all(char in list(j) for char in right):
					digits.append('3')
				elif all(char in list(j) for char in four_arm):
					digits.append('5')
				elif (bool(right[0] in j) != bool(right[1] in j)):
					digits.append('2')
			elif len(j) == 6:
				if all(char in list(j) for char in right) and all(char in list(j) for char in four_arm):
					digits.append('9')
				elif all(char in list(j) for char in four_arm):
					digits.append('6')
				elif (bool(four_arm[0] in j) != bool(four_arm[1] in j)):
					digits.append('0')
				else: print('confusion')
		sequences.append(int(''.join(digits)))
	return sequences

sequences = get_sequences(inputs)
print(sum(sequences))

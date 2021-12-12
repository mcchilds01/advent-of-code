with open('input_7.txt', 'r') as f:
	inputs =  [i.strip().split(',') for i in f]
	inputs = [int(i) for i in inputs[0]]

maximum = max(inputs)
minimum = min(inputs)

def get_alignment_one():
	leader = [maximum] * len(inputs)
	for i in range(minimum, maximum+1):
		candidate_alignment = []
		for j in inputs:
			candidate_alignment.append(abs(i-j))
		if sum(candidate_alignment) < sum(leader):
			leader = candidate_alignment
			candidate_alignment = []
	return sum(leader)

alignment_one = get_alignment_one()
print(alignment_one)

####################################

def get_alignment_two():
	leader = [sum([i for i in range(maximum+1)])] * len(inputs)
	candidate_alignment = []
	for i in range(minimum, maximum+1):
		candidate_alignment = []
		for j in inputs:
			candidate_alignment.append(sum([i for i in range(abs(i-j)+1)]))
		if sum(candidate_alignment) < sum(leader):
			leader = candidate_alignment
			candidate_alignment = []
	return sum(leader)

alignment_two = get_alignment_two()
print(alignment_two)

with open('input_10.txt', 'r') as f:
	inputs =  [i.strip() for i in f]

# print(inputs)

openers = ['[', '{', '(', '<']
closers = [']', '}', ')', '>']

pairs = {closers[i]: openers[i] for i in range(len(openers))}
closers_dict = {openers[i]: closers[i] for i in range(len(openers))}

def get_syntax_errors(input_string):
	errors = []
	key = []
	for i in input_string:
		if i in openers:
			key.append(i)
		elif i in closers:
			if key[-1] != pairs[i]:
				return i
			else: key.pop()
	return [closers_dict[key[i]] for i in range(len(key)-1, -1, -1)]

def get_syntext_error_score(inputs):
	illegal_characters = []
	completion = []
	score_1 = 0 
	for i in inputs:
		response = get_syntax_errors(i)
		if len(response) == 1:
			illegal_characters.append(response)
		else: 
			completion.append(response)

	for i in illegal_characters:
		if i == ')':
			score_1 += 3
		elif i == ']':
			score_1 += 57
		elif i == '}':
			score_1 += 1197
		elif i == '>':
			score_1 += 25137

	completion_scores = []
	for i in completion:
		score = 0
		for j in i:
			score *= 5
			if j == ')':
				score += 1
			elif j == ']':
				score += 2
			elif j == '}':
				score += 3
			elif j == '>':
				score += 4
		completion_scores.append(score)

	return score_1, sorted(completion_scores)[int(len(completion_scores)/2)]

score_1, score_2 = get_syntext_error_score(inputs)
print(score_1, score_2)



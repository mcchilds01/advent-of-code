#Part One

with open('input_1.txt', 'r') as f:
	input_list = [x.strip() for x in f]

increases = [input_list[i] for i in range(len(input_list)) if int(input_list[i]) > int(input_list[i-1])]
print(len(increases))

#Part Two

increases_2 = [i for i in range(len(input_list)-3) if (int(input_list[i]) + int(input_list[i+1]) + int(input_list[i+2])) < (int(input_list[i+1]) + int(input_list[i+2]) + int(input_list[i+3]))]
print(len(increases_2))
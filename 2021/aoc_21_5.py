with open('input_5.txt', 'r') as f:
	inputs =  [i.strip().split(' -> ') for i in f]

def transform_inputs(inputs):
	for line_segment in range(len(inputs)): 
		for point in range(len(inputs[line_segment])):
			inputs[line_segment][point] = tuple(inputs[line_segment][point].split(','))
	return inputs

def get_max_dimension(inputs):
	max_dimension = 0
	for i in inputs:
		for j in i:
			for k in j:
				if int(k) > max_dimension:
					max_dimension = int(k)
	return max_dimension+1

def create_grid(dimension):
	grid = []
	for i in range(int(dimension)):
		grid.append([0] * int(dimension))
	return grid 

def get_lines(inputs, grid):
	for i in inputs:
		if i[0][0] != i[1][0] and i[0][1] != i[1][1]:
			pass
		else: 
			if i[0][0] == i[1][0]:
				x = int(i[0][0])
				y1 = min(int(i[0][1]), int(i[1][1]))
				y2 = max(int(i[0][1]), int(i[1][1]))
				for j in range(y1, y2+1):
					grid[j][x] += 1
			elif i[0][1] == i[1][1]:
				start = min(int(i[0][0]), int(i[1][0]))
				end = max(int(i[0][0]), int(i[1][0]))
				for j in range(start, end+1):
					grid[int(i[0][1])][j] += 1
	return grid

def get_tally(grid_complete):
	tally = 0
	for i in grid_complete:
		for j in i:
			if j >= 2:
				tally +=1 
	return tally

inputs = transform_inputs(inputs)
max_dimension = get_max_dimension(inputs)
grid = create_grid(max_dimension)
grid_complete = get_lines(inputs, grid)
tally = get_tally(grid_complete)

print("Final tally: ", tally)

######################################################

def get_lines_2(inputs, grid):
	for i in inputs:
		if i[0][0] != i[1][0] and i[0][1] != i[1][1]:
			points = []
			x1, x2 = int(i[0][0]), int(i[1][0])
			y1, y2 = int(i[0][1]), int(i[1][1])
			points.append((x1,y1))
			if (x1 < x2):
				for j in range(x1, x2):
					if y1 < y2:
						new_point = (x1+1, y1+1) 
					elif y1 > y2:
						new_point = (x1+1, y1-1) 
					points.append(new_point)
					x1, y1 = new_point[0], new_point[1]
			else: 
				for j in range(int(i[1][0]), int(i[0][0])):
					if (x1 > x2) and (y1 < y2):
						new_point = (x1-1, y1+1) 
					else:	
						new_point = (x1-1, y1-1) 
					points.append(new_point)
					x1, y1 = new_point[0], new_point[1]
			for point in points:
				grid[point[1]][point[0]] += 1
		else: 
			if i[0][0] == i[1][0]:
				x = int(i[0][0])
				y1 = min(int(i[0][1]), int(i[1][1]))
				y2 = max(int(i[0][1]), int(i[1][1]))
				for j in range(y1, y2+1):
					grid[j][x] += 1
			elif i[0][1] == i[1][1]:
				start = min(int(i[0][0]), int(i[1][0]))
				end = max(int(i[0][0]), int(i[1][0]))
				for j in range(start, end+1):
					grid[int(i[0][1])][j] += 1
	return grid

grid_2 = create_grid(max_dimension)
grid_2_complete = get_lines_2(inputs, grid_2)
tally = get_tally(grid_2_complete)
print("Final tally part 2: ", tally)

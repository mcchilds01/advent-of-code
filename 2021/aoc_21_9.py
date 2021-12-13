with open('input_9.txt', 'r') as f:
	inputs =  [[int(j) for j in i.strip()] for i in f]

def get_neighbors(point, i, j):
	neighbors = [point]
	try:
		if i-1 >= 0:
			top = inputs[i-1][j]
			neighbors.append(top)
	except:
		pass
	try: 
		bottom = inputs[i+1][j]
		neighbors.append(bottom)
	except: 
		pass
	try: 
		if j-1 >= 0:
			left = inputs[i][j-1]
			neighbors.append(left)
	except:
		pass
	try:
		right = inputs[i][j+1]
		neighbors.append(right)
	except:
		pass
	return neighbors

def get_low_points(inputs):
	low_points_coords = []
	low_points = []
	for i in range(len(inputs)):
		for j in range(len(inputs[i])):
			point = inputs[i][j]
			neighbors = get_neighbors(point, i, j)
			if min(neighbors) == point:
				if neighbors.count(point) == 1:
					low_points.append(point)
					low_points_coords.append((i, j))
	return low_points_coords, (sum(low_points) + len(low_points))

low_points_coords, answer = get_low_points(inputs)
print(answer)

####################################################################

checked = []

def get_neighbors_2(point):
	i = point[0]
	j = point[1]
	neighbors = []
	try:
		if i-1 >= 0:
			top = inputs[i-1][j]
			if top != 9:
				neighbors.append((i-1, j))
	except:
		pass
	try: 
		bottom = inputs[i+1][j]
		if bottom != 9:
			neighbors.append((i+1, j))
	except: 
		pass
	try: 
		if j-1 >= 0:
			left = inputs[i][j-1]
			if left != 9:
				neighbors.append((i, j-1))
	except:
		pass
	try:
		right = inputs[i][j+1]
		if right != 9:
			neighbors.append((i, j+1))
	except:
		pass
	return neighbors

def get_neighbors_recursive(point):
	global checked
	neighbors = []
	if not point in checked:
		neighbors += get_neighbors_2(point)
		checked.append(point)
		if neighbors != None:
			for neighbor in neighbors:
				neighbors += get_neighbors_recursive(neighbor)
			return list(set(neighbors))
		else: return []
	else: return []

sizes = []
for low_point in low_points_coords:
	basin = get_neighbors_recursive(low_point)
	sizes.append(len(basin))

top_3 = sorted(sizes, reverse=True)[:3]
product = 1
for i in top_3:
	product *= i

print(product)

# CSE 2050
# Knights

def knight_moves(position):
	position_adjust = [-1,1,-2,2]
	position_list = []

	for i in position_adjust:
		for j in position_adjust:
			if j != abs(i):
				x = (position[0] + j, position[1] + i)
				position_list.append(x)
	
	new_list = []
	for i in position_list:
		x = abs(position[0] - i[0]) + abs(position[1] - i[1])
		if x == 3:
			new_list.append(i)
	new_list2 = []
	for i in new_list:
		l = 0
		for j in i:
			t = 0
			if j > 8 or j < 1:
				l = 1
		if l == 0:
			new_list2.append(i)
	return new_list2

def knight_move(k_position, p_position):
	moves = knight_moves(k_position)
	for i in moves:
		if i == p_position:
			return True
	return False

def find_moves(k_position, p_list):
	if p_list is None:
		return True
	poss_moves = set()
	kth = knight_moves(k_position)
	for i in p_list:
		if i in kth:
			poss_moves.add(i)
	return poss_moves

def iterate_moves(p_list, net):
	new_list = []
	for i in net:
		if len(i) == len(p_list):
			return True
		x = [i for i in p_list]
		for q in i:
			x.remove(q)
		move = find_moves(i[-1], x)
		if move is not None:
			for mover in move:
				newer = [m for m in i]
				newer.append(mover)
				new_list.append(newer)
		else:
			return []
	return new_list

def solvable(k_position, p_list):
	start_net = find_moves(k_position, p_list)
	if start_net == []:
		return False
	test_lisp = [[i] for i in start_net]
	status = False
	while status is not [] or status is not True:
		x = [i for i in p_list]
		status = iterate_moves(x, test_lisp)
		test_lisp = status
		if status is True:
			return True
		if status == []:
			return False

def create_board_list(var = 8):
	board_list = []
	var += 1
	for i in range(var):
		if i == 0:
			pass
		else:
			for j in range(var):
				if j == 0:
					pass
				else:
					x = (i,j)
					board_list.append(x)
	return board_list

def findstart(p_list):
	recurse_board = create_board_list()
	output_set = set()
	for i in recurse_board:
		x = set(i for i in p_list)
		test = solvable(i,x)
		if test is True:
			output_set.add(i)
	
	return output_set

def findpath(k_position, p_list, prev_moves):
	if p_list is None:
		return prev_moves
	for i in p_list:
		if knight_move(k_position, i):
			return findpath(i, p_list.remove(i), prev_moves.append(i))
	return None
t = {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4), (5,5), (5,6), (5,7), (6,5), (6,7), (7,5), (7,6), (7,7)}
t2 = (2,7)


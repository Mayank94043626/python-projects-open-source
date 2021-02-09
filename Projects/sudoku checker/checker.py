#!python3
# -*- coding: utf-8 -*-

import sys

#print the sudoku map
def print_board(x):
	global error
	print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

	for i in range(9):
		print("║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║".format(x[i][0],
			x[i][1],
			x[i][2],
			x[i][3],
			x[i][4],
			x[i][5],
			x[i][6],
			x[i][7],
			x[i][8],))

		if i != 8:
			print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

	if error:
		print("╚═══╧═══╧═══INVALID INPUT!══╧═══╧═══╝")

	else:
		print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

#checks if the sudoku map is correct
def check(a):
	lst = []
	for i in range(9):

		#checks each row
		for j in range(1,10):
			if a[i].count(j) > 1:
				return False

		#checks each column
		for l in range(1,10):
			if lst.count(l) > 1:
				return False
		lst.clear()
		for k in range(9):
			lst.append(a[k][i])

	return True

#gets input
def get_input():
	global error, x, y
	try:
		#cleares the previous input
		print(' '*64)
		sys.stdout.write("\033[F")

		inp = input("Input: ")
		if (len(inp) == 1) and (inp != "0"):
			board[x][y] = int(inp)
			error = False
		else:
			raise ValueError
	except:
		error = True

#moves the terminal index back to the start of the map
def move_index():
	for i in range(20):
		sys.stdout.write("\033[F")

board = [
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
]

error = False

#printing the sudoku map while refreasing it each input
for x in range(9):
	for y in range(9):

		print_board(board)

		get_input()
		
		#if an invalid input is given it loops untill a correct input is given
		while error:
			move_index()
			print_board(board)
			get_input()

		move_index()

#when getting the input is done print and check the board
print_board(board)
if check(board):
	print("Correct Sudoku Board!")

elif not(check(board)):
	print("Incorrect Sudoku Board!")
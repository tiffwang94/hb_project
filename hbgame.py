print
print "Welcome to this game of Connect Four!"
print
print "........"
print
print "Player one, what is your name?"
print

playerone = raw_input("Player one > ")
playerone = playerone.capitalize()
print
print "Hello, {}!".format(playerone)
print
print "Player two, what is your name?"
print

playertwo = raw_input("Player two > ")
playertwo = playertwo.capitalize()

print
print "Hello, {}!".format(playertwo)
print
print "The object of this game is to connect four letters in a row, either horizontally or vertically."
print "Each player must choose a column, numbered at the bottom of the board. The first play to four in a row wins!"
print
print "Player one will always go first."
print
print "{}, you will be letter 'X' and {}, you will be letter 'O'".format(playerone, playertwo)
print

#variables for starting state of the game
count = [0,0,0,0,0]

rows = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]

current_player = "X"

game_continues = True

diagonal_wins = [
	[(0,0), (1,1), (2,2), (3,3)],
	[(1,1), (2,2), (3,3), (4,4)],
	[(0,1), (1,2), (2,3), (3,4)],
	[(1,0), (2,1), (3,2), (4,3)],
	[(0,4), (1,3), (2,2), (3,1)],
	[(1,3), (2,2), (3,1), (4,0)],
	[(0,3), (1,2), (2,1), (3,0)],
	[(1,4), (2,3), (3,2), (4,1)]]


def print_board():
	print "| {} | {} | {} | {} | {} |".format(rows[4][0], rows[4][1], rows[4][2], rows[4][3], rows[4][4])
	print "----------------------"
	print "| {} | {} | {} | {} | {} |".format(rows[3][0], rows[3][1], rows[3][2], rows[3][3], rows[3][4])
	print "----------------------"
	print "| {} | {} | {} | {} | {} |".format(rows[2][0], rows[2][1], rows[2][2], rows[2][3], rows[2][4])
	print "----------------------"
	print "| {} | {} | {} | {} | {} |".format(rows[1][0], rows[1][1], rows[1][2], rows[1][3], rows[1][4])
	print "----------------------"
	print "| {} | {} | {} | {} | {} |".format(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
	print "----------------------"
	print "- 0 - 1 - 2 - 3 - 4-"

# if rows[0][0] == current_player and rows[1][1] == current_player and rows [2][2] == current_player:
# 	if 	rows[1][1] == current_player and rows[2][2] == current_player and rows[3[]3] == current_player and rows[4][]4] == current_player:
# 		if rows[0][1] == current_player and rows[1][2] == current_player and rows[2][3] == current_player and rows[3][4] == current_player:
# 			if rows[1][0] == current_player and rows[2][1] == current_player and rows[3][2] == current_player and rows[4][3] == current_player:
# 				if rows[0][4] == current_player and rows[1][3] == current_player and rows[2][2] == current_player and rows[3][1] == current_player:
# 					if rows[1][3] == current_player and rows[2][2] == current_player and rows[3][1] == current_player and rows[4][0] == current_player:
# 						if rows[0][3] == current_player and rows[1][2] == current_player and rows[2][1] == current_player and rows[3][0] == current_player:
# 							if rows[1][4] == current_player and rows[2][3] == current_player and rows[3][2] == current_player and rows[4][1] == current_player:


def check_valid(column):
	if count[column] < 6:
		return True
	else:
		return False

def check_valid(row):
	if count[row] < 6:
		return True
	else:
		return False


def update_board(column, current_player):
	row = count[column]
	rows[row][column] = current_player
	count[column] = count[column] + 1
	print current_player

	print_board()
	
def check_for_win(current_player):
	horizontal_counter = 0
	vertical_counter = 0
	for row in range(5):
	 	for column in range(5):
	 		if rows[row][column] == current_player:
	 			horizontal_counter += 1
	 		elif rows[column][row] == current_player:
	 			vertical_counter += 1
	 		elif horizontal_counter == 4 or vertical_counter == 4:
	 			return True
	 		else:
	 			horizontal_counter = 0
	 			vertical_counter = 0
	 		#above is option number 2 given

	for diag in diagonal_wins:
		counter = 0
		for coordinate in diag:
			row = coordinate[0]
			column = coordinate[1]
			if rows[row][column] == current_player:
				counter += 1
			else:
				counter = 0
			if counter == 4: 
				#this bit is for the diagonal wins
				print counter
				return True 


def switch_players(player):
	if player == "X":
		return "O"
	else:
		return "X"



while game_continues == True:
	print_board()
	print "{}, it is your turn.".format(current_player)
	p_one_choice = int(raw_input("Please choose a column. > "))


	while check_valid(p_one_choice) == False:
		p_one_choice = raw_input("That's not a valid column. Please choose another one. ")
	update_board(p_one_choice, current_player)

	if check_for_win(current_player): 
		print "Game over. Good job, {} !".format(current_player)
		game_continues = False
	current_player = switch_players(current_player)




# print "| {} | {} | {} | {} | {} |".format(rows[4][0], rows[4][1], rows[4][2], rows[4][3], rows[4][4])
# print "-----------------"
# print "| {} | {} | {} | {} | {} |".format(rows[3][0], rows[3][1], rows[3][2], rows[3][3], rows[3][4])
# print "-----------------"
# print "| {} | {} | {} | {} | {} |".format(rows[2][0], rows[2][1], rows[2][2], rows[2][3], rows[2][4])
# print "-----------------"
# print "| {} | {} | {} | {} | {} |".format(rows[1][0], rows[1][1], rows[1][2], rows[1][3], rows[1][4])
# print "----------------"
# print "| {} | {} | {} | {} | {} |".format(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
# print "---------------"
# print "- 0 - 1 - 2 - 3 - 4--"
# print 
# print "{}, you will be starting first, please choose a column.".format(playerone)
# print "........"


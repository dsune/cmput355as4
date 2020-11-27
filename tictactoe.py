import random
import time
import sys

# initiates global variables
ttt_board = ["_", "_", "_",
			 "_", "_", "_",
			 "_", "_", "_"]

positions = ["1", "2", "3",
			 "4", "5", "6",
			 "7", "8", "9",]

player_chars = ["X", "O"]
game_done = False

# main function used to play the game
def play():
	global game_done
	global ttt_board

	# randomizes which player will start the game
	print("The game will randomly choose which player will start.")
	current_player = random.randint(0, 1)
	print("\nRandomizing...")
	time.sleep(1.5)
	print("\nPlayer " + player_chars[current_player] + " will go first!")

	show_board()

	# loop that will run until someone wins
	while not game_done:
		player_turn(current_player)

		if check_win() == True:
			game_done = True

		if not game_done:
			if player_chars[current_player] == "X":
				current_player = 1
			elif player_chars[current_player] == "O":
				current_player = 0

	# checks if board is full or not
	# if board is full and no winner has been declared, game must be a draw
	if "_" not in ttt_board:
		print("This game ends in a draw.")
		play_again()
	else:
		print("\nPlayer " + player_chars[current_player] + " wins!")
		play_again()

# displays the current state of the board
def show_board():
	print("\n")
	print("-------------")
	print("| " + ttt_board[0] + " | " + ttt_board[1] + " | " + ttt_board[2] + " |")
	print("| " + ttt_board[3] + " | " + ttt_board[4] + " | " + ttt_board[5] + " |")
	print("| " + ttt_board[6] + " | " + ttt_board[7] + " | " + ttt_board[8] + " |")
	print("-------------")
	print("\n")

# handles each player's turn
def player_turn(player):
	global turn_count
	global positions
	global game_done

	# initial input from player, choosing their desired move
	chosen_pos = input("Make your move! Choose a position on the board (1-9): ")
	valid_pos = False
	
	# checks if the inputted position is a valid move on the board
	while valid_pos == False:

		if chosen_pos not in positions:
			chosen_pos = input("\nSorry, that spot doesn't exist on the board! \nPlease choose a position from 1-9: ")
		elif ttt_board[int(chosen_pos) - 1] == "_":
			valid_pos = True
		else:
			chosen_pos = input("\nOops! That spot is already taken, try another one between 1-9: ")

	# updates the board to reflect the player's move
	ttt_board[int(chosen_pos) - 1] = player_chars[player]

	show_board()

# checks each possible win condition
def check_win():
	if check_diag() or check_row() or check_col():
		return True
	else:
		return False

# checks diagonals for wins
def check_diag():

	if ttt_board[0] == ttt_board[4] == ttt_board[8] != "_":
		return True
	elif ttt_board[2] == ttt_board[4] == ttt_board[6] != "_":
		return True
	else:
		return False

# checks rows for wins
def check_row():

	if ttt_board[0] == ttt_board[1] == ttt_board[2] != "_":
		return True
	elif ttt_board[3] == ttt_board[4] == ttt_board[5] != "_":
		return True
	elif ttt_board[6] == ttt_board[7] == ttt_board[8] != "_":
		return True
	else:
		return False

# checks columns for wins
def check_col():

	if ttt_board[0] == ttt_board[3] == ttt_board[6] != "_":
		return True
	elif ttt_board[1] == ttt_board[4] == ttt_board[7] != "_":
		return True
	elif ttt_board[2] == ttt_board[5] == ttt_board[8] != "_":
		return True
	else:
		return False

# asks if the players would like to play again after a win/loss/draw
def play_again():
	global ttt_board
	global game_done

	play_choice = input("Play again? (Y or N): ")
	play_choices = ["Y", "N"]

	while play_choice not in play_choices:
		print("Please input a valid choice!")
		play_choice = input("Play again? (Y or N): ")

	# resets the board and and the game status
	if play_choice == "Y":
		ttt_board = ["_", "_", "_",
		 			 "_", "_", "_",
		 			 "_", "_", "_"]
		game_done = False
		play()

	# ends the program if no more games are to be played
	elif play_choice == "N":
		sys.exit()

play()
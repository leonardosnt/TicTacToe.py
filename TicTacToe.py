import os, sys

PLAYER_CHAR 	= ['X', 'O']
WIN_IDX 		= [[0, 1, 2 ], [3, 4, 5 ], [ 6, 7, 8 ], [ 0, 3, 6 ], [ 1, 4, 7 ], [ 2, 5, 8 ], [ 2, 4, 6 ], [ 0, 4, 8 ]]

table 			= [''] * 9
player 			= 0

def print_table():
	os.system("cls")

	print("Joguin da velha by leozin\n")

	for x in range(0, 9):
		endl = "\n" if x % 3 == 2 else "" 

		print("[" + table[x] + "]", end=endl)

def check_win():
	for i in range(0, 8):
		p1 = WIN_IDX[i][0] 
		p2 = WIN_IDX[i][1] 
		p3 = WIN_IDX[i][2]

		for p in range(0, 2):
			if (table[p1] == PLAYER_CHAR[p] and table[p2] == PLAYER_CHAR[p] and table[p3] == PLAYER_CHAR[p]):
				
				for x in range(0, 9):
					char = PLAYER_CHAR[p] if (x == p1 or x == p2 or x == p3) else " "
					table[x] = char

				print_table()

				print("\nJogador " + str(p + 1) + " [" + PLAYER_CHAR[p] + "] " + "Venceu!!")

				ans = input("\nDeseja reiniciar? S ou N: ")

				if (ans.upper() == "S"):
					main()
				else:
					sys.exit(0)
def start():
	player = 1

	for x in range(0, 9):
		table[x] = ' '

def main():
		start()

		while (True): 
			print_table()

			expr = True;

			while (expr):
				expr = False

				try:
					print ("\nVez do jogador " + str(player + 1) + " [" + PLAYER_CHAR[player] + "]")
					pos = int(input("Digite uma posicao de 1 a 9: "))

					if (pos > 9 or pos < 1 or  table[pos - 1] != ' '):
						raise
					break
				except Exception as e:
					print("Posicao invalida ou ocupada!")
					expr = True

			table[pos - 1] = PLAYER_CHAR[player]

			global player
			player = 0 if player == 1 else 1

			check_win()

if __name__ == "__main__": 
	main()

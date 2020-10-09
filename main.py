def make_2d_list(x, y, default_data):
	my_list = list()
	for i in range(y):
		nested_list = list()
		for j in range(x):
			nested_list.append(default_data)
		my_list.append(nested_list)
	return my_list

class whatever_you_want:
	def __init__(self):
		self.grid = make_2d_list(3, 3, 0)
		self.player: int = 1
		self.lookup: dict = {
			1: (0,0), 2: (0,1), 3: (0,2),
			4: (1,0), 5: (1,1), 6: (1,2),
			7: (2,0), 8: (2,1), 9: (2,2)
		}
	
	def reset(self):
		self.grid = make_2d_list(3, 3, 0)
		
	def get_input(self):
		while True:
			line = input("Please input 1 - 9: ")
			try:
				number = int(line)
				if not (1 <= number <= 9):
					print("Number not between 1 and 9.")
					continue
				i,j = self.lookup[number]
				if self.grid[i][j] != 0:
					print("Spot already played.", j, i)
					self.print_grid()
					continue
				return number
			except Exception as e:
				print("Bad input.", e)
	
	def print_grid(self):
		for nested_list in self.grid:
			for data in nested_list:
				if data == 0:
					print("_", end=" ")
				elif data == 1:
					print("X", end=" ")
				elif data == 2:
					print("O", end=" ")
				else:
					assert(0, "Only 0, 1, 2.")
			print()
			
	def switch_player(self):
		if self.player == 1:
			self.player = 2
		elif self.player == 2:
			self.player = 1
		else:
			assert(0, "This is a two player game.")
			
	def place_token(self, p_input):
		i,j = self.lookup[p_input]
		if self.grid != 0:
			self.grid[i][j] = self.player
		
	def play_game(self):
		print("Welcome to Tic-Tac-Toe!")
		for i in range(9):
			self.print_grid()
			p_input = self.get_input()
			self.place_token(p_input)
			if self.player_has_won():
				print(f"Player {self.player} has won!")
				break
			self.switch_player()
			
	def player_has_won(self) -> bool:
		victory_lookup = [
			[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]
		]
		for sublist in victory_lookup:
			i,j = self.lookup[sublist[0]]
			k,l = self.lookup[sublist[1]]
			m,n = self.lookup[sublist[2]]
			if self.grid[i][j] == self.grid[k][l] == self.grid[m][n] == self.player:
				return True
		return False
	
if __name__ == "__main__":
	game = whatever_you_want()
	while True:
		game.play_game()
		game.reset()
		while True:
			answer = input("Play again? Y/N ")
			if answer in ("Y","y"):
				break
			elif answer in ("N","n"):
				print("Goodbye!")
				exit(0)
			else:
				print("Y or N only please")

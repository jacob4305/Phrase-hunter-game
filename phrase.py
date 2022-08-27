class Phrase:
	
	def __init__(self, phrase):
		self.phrase = phrase.lower()


	def __str__(self):
		return f'phrase object-{self.phrase}'


	def display(self, guesses_list):
		for letter in self.phrase:
			if letter in guesses_list:
				print(f'{letter}', end="")
			else:
				print("_", end="")
		print("\n")

		
	def check_letter(self, letter):
		self.letter_list = []
		for le in self.phrase:
			self.letter_list.append(le)
		if letter in self.letter_list:
			print("True")
		if letter not in self.letter_list:
			print("False")


	def check_complete(self, guesses_list):
		"""checks if the self.game_guesses/display is filled out and returns False"""
		c = 0
		for letter in self.phrase:
			if letter in guesses_list:
				c += 1
		if c == len(self.phrase):
			return "end loop"

from phrase import Phrase 
import random


class Game:
	def __init__(self):
		self.game_guesses = [' ']
		self.phrase_list = [
			Phrase('cost an arm and a leg'),
			Phrase('A piece of cake'),
			Phrase('Let the cat out of the bag'),
			Phrase('feel under the weather'),
			Phrase('kill two birds with one stone'),
	]
		self.active_phrase = None 
		self.misses = 0


	def __str__(self):
		return f'{self.phrase}'


	def missed(self):
		"""tracks the number of incorrect guesses"""
		count = 0
		for letter in self.game_guesses:
			if letter not in self.active_phrase.phrase:
				count += 1
				self.misses =+ count
			if self.misses == 5:
				return "end loop"	
		return


	def start(self):
		"""contains the main game loop"""
		Game.welcome(self)
		Game.get_random_phrase(self) 
		while True: 
			print("You have {} lives left".format(5 - self.misses))
			self.active_phrase.display(self.game_guesses)
			Game.get_guess(self)
			Game.missed(self)
			self.active_phrase.check_complete(self.game_guesses)
			if self.active_phrase.check_complete(self.game_guesses) == "end loop":
				print("You got it!!!")
				break
			if Game.missed(self) == "end loop":
				print("Bummer looks like you ran out of lives")
				break
		print(f'{self.active_phrase.phrase} was the correct awnser!')
		play_again = input("Do you want to play again?(y/n)~~> ").lower()
		if play_again == "y":
			self.game_guesses.clear()
			self.game_guesses.append(' ')
			self.misses = 0
			Game.start(self)
		else:
			Game.game_over(self)


	def get_random_phrase(self):
		"""random retrieves a phrase to use in the game"""
		random_phrase = random.choice(self.phrase_list)
		self.active_phrase = random_phrase
		return random_phrase


	def welcome(self):
		"""prints a welcome message to the user"""
		print("~~~Welcome to Phrase hunters!!!~~~")
	 

	def get_guess(self):
		"""gets the guess from the user and records it"""
		while True:
			guess = input("enter letter here:~~>  ").lower()
			try:
				guess = int(guess)
				print("Numbers are not allowed, please enter a letter")
				self.active_phrase.display(self.game_guesses)
				continue
			except ValueError:
				print("\n")
				if guess.isalpha() == True:
					if len(guess) == 1:
						self.game_guesses.append(guess)
						break
				if len(guess) > 1:
					print("Please enter a single letter")
					self.active_phrase.display(self.game_guesses)
				else:
					print("Please enter a letter")
					self.active_phrase.display(self.game_guesses)
		return


	def game_over(self):
		"""prints a game over message"""
		print("Thanks for playing!!!")

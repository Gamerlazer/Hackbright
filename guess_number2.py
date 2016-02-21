
# Generates random number
import random
set_number = random.randrange(1,101)

# Prompts the user for their first guess
user_guess = int(raw_input("Please guess an integer from 1 - 100: "))
guessed_numbers = []

def guessing_game(user_guess):
	while user_guess != set_number:
	# Checks to make sure number was not already guessed
		if user_guess in guessed_numbers:
			user_guess = int(raw_input("You've already guessed %i! Please guess another integer from 1 - 100: " % user_guess))
	# If too low, adds guess to list and asks user for another guess
		elif user_guess < set_number:
			guessed_numbers.append(user_guess)
			user_guess = int(raw_input("%i is too low. Please guess another integer from 1 - 100: " % user_guess))
	# If too high, adds guess to list and asks user for another guess
		else:	
			guessed_numbers.append(user_guess)
			user_guess = int(raw_input("%i is too high. Please guess an integer from 1 - 100: " % user_guess))
	# If user only needed one guess
	if len(guessed_numbers) == 0:
		print "Yay! %i is the right number! It only took you 1 guess!" % (user_guess)
	# If user needed multiple guesses
	else:
		print "Yay! %i is the right number! It took you %i guesses!" % (user_guess,len(guessed_numbers)+1)

guessing_game(user_guess)



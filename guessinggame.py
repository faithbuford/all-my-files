import random 

mysteryNum = random.randint(1, 100)
score = 0 

while True:
	guess = int(input("Pick a number between 1 and 100: "))
	score = score + 1 

	if guess == mysteryNum: 
		print("good guess, you win")
		break
	elif guess > mysteryNum:
		print("Too high, try again")
	else: 
		print("too low, try again")

print("it took you " + str(score) + " guesses")
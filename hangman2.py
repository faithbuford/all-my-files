import random
theList = ["computer", "weird", "granted", "superb", "fairy"]
word = random.choice(theList)

print("welcome to the hangman game")
yourMisses = input("enter the number of misses you'd like before the game ends: ")

myString = word 
theWord = list(myString)
correctLetters = []
wrongLetters = []
guessList = []

misses = 0

for letter in theWord:
	correctLetters.append("_")
print(correctLetters)

while True:
	letter = input("enter a letter: ")
	if letter in word:
		print("letter is in word")
		index = theWord.index(str(letter))
		correctLetters.pop(int(index))
		correctLetters.insert(int(index), letter)
		guessList.append(letter)
		print(correctLetters)
		print("you've guessed " + str(guessList))
	else:
		print("letter is not in word")
		misses = misses + 1
		
	
	#if misses == int(yourMisses)
		#print("game over")
		#print("your mystery word was: " + word)
	if correctLetters = word:
		print("congratulations, you won !")
import random
theList = ["sneeze", "weird", "granted", "superb", "animation"]
word = random.choice(theList)


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
		correctLetters.append(letter)
		print(guessList)
		print("you've guessed " + str(guessList))
	else:
		print("letter is not in word")
	print
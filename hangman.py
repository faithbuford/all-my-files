myWord = "hello"

choice = input("type a word: ")

if choice == myWord:
	print("it's a match")
else:
	print("not a match")


# how to check if a letter is in a word 

letter = input("enter a letter: ")

if letter in myWord:
	print("letter is in word")
else:
	print("letter is not in word")

count = 0

for letter2 in myWord:
	if letter2 == letter:
		print(count) 
	count += 1 



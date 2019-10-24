# faith buford
# first hour 
# 10 / 16


# make a variable to hold your list 
print("welcome to To Do List")
todoList = []
while True: 
	print("enter a to add an item")
	print("enter r to remove an item")
	print("enter p to print the list")
	print("enter q to quit")
	choice = input("choose: ")

	if choice == "q":
		break
	elif choice == "a":
		mytodo = input("what would you like to add to your to do list? ")
		todoList.append(mytodo)
		
	elif choice == "r":
		mytodo = input("what would you like to remove? ")
		todoList.remove(mytodo)
	elif choice == "p":
		print(todoList)
		
	else:
		print("you chose something not listed")
favFoods = ["Pizza", "Ice Cream", "Noodles"]
print(favFoods[0])
print(favFoods[2])
print(favFoods)
# adds to the end of the list 
favFoods.append("Yogurt")
print(favFoods)
print(favFoods[3])
print("My fourth favorite food is " + favFoods[3])
# insert - adds to an index in a list 
favFoods.insert(1, "Chicken")
print(favFoods)
# remove an item from the list 
favFoods.remove("Chicken")
print(favFoods)
# remove by index 
favFoods.pop(0)
print(favFoods)

favFoods.insert(0, "pizza")
# loop through a list 
for food in favFoods:
	print(food)

numList = [1, 2 , 3, 4 , 5, 6, 7, 8]

# Loop through the list and add all the numbers together then print the sum

sum = 0 
for num in numList:
	sum = sum + num 
print(sum)
# function to get the length of a list 
print(len(numList))

# make a list for fav movies 
# prompt for a favorite movie 

myfood = input("what is your favorite food?")
favFoods.append(myFood)
print(favFoods)

myMovies = ["suite francaise", "interstellar", "scream"]
yourMovie = input("what is your favorite movie ? ")
myMovies.append(yourMovie)
print(myMovies)

# list methods and functions 
# append - adds an item to the end of a list 
# insert - adds an item to a specified index 
# remove - removes a specified item from a list 
# pop - removes an item from a specified index
# len - returns the length of the list 
print(favFoods[len(favFoods)- 1])
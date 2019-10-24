#conditionals 

age = input("what is your age? ") # prompt for age

# check if the age is more that 17. if so, person can see
# R rated movies
age = int(age)
if age > 17: # everything in the if statement only runs if the condition is true
	print("you can see an R rated movie")

else: 
	print("you cannot see an r rated movie, too bad, so sad")

print("Have a nice day!")
# you can check all these conditions
# >, <, >=, <=, == (== means equal too)

birthday = input("Is today your birthday ? (yes or no) ")
if birthday == "yes":
	print("happy birthday")

print("have a nice day")

myNum = 7
guess = input("guess a number between 1 and 10")
guess = int(guess)
if guess == myNum:
	print("you guessed correctly")
elif guess > myNum:
	print("too high")
else: 
	print("too low")
print("thanks for playing")
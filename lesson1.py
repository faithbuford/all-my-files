# calculations, printing, variables

# Printing to the screen
# The built in function print(), prints to the screen 
# it will print both Strings and numbers 
print("Printing to the Screen...")
print("hello") #a string
print('hello again')
print(6) # a number 
print("6") # a string again
print(6 + 6) # 12
print("6" + "6") # string concationation
# print("6" + 6) #what will this do? -> errror

# performing calculations 
# addition + 
# subtraction -
# multiplication *
# division /
# exponents **
# modulo %

print(4 - 2) # subtraction
print(4 * 2) # multiplication
print(4 / 3) # division
print(4** 3) # exponents 
print("modulo operator test")
print(5 % 3)
print(10 % 2)
print(16 % 3)
# modulo gives remainders 
# python operators follow the same order of operations as Math 
print(4 - 2 * 2) #should give zero 
print((4 - 2) * 2) # should give 4 

# variables 
# variables are used to hold data 
# variables are declared and set to a value (initializing)
badLuck = 13 # declared a variable called badLuck and initialized it to 13 
# i can print the variable using its name 
print("badLuck = " + str(badLuck)) # cast it to a string 
# lets do another one 
goodLuck = "4" # String variable 
print("goodLuck = " + goodLuck) # don't have to cast 
badLuck + 5 # pointless
print(badLuck)
badLuck = badLuck + 5 # now badLuck is 18
print(badLuck)

# you can also save input into variables 
# using input(), a prompt goes inside the ()
name = input("What is your name? ")
print("Hello" + name)
print(name * 10)
name = name + "\n" #escape character (newline)
print(name * 10)
#let's try some math 
base = input("Enter the base number: ")
exp = input("Enter the exponent: ")
print(int(base) ** int(exp))
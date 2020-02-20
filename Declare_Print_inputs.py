# Declare a variable and initialize it
#Integer
f = 99 
print(f)
#String
g = 'Hello!'
print(g)
#Concatenate
a="AK"
b = 47
#print (a+b) #Error! Cannot add two different types. Comment to run without errors
a="AK"
b = 47
print (a+str(b)) #Correct

#printing
print("hello!")

name = "Saloni"
name2 = "John"
#2 ways of printing variables
print(name, "and", name2, "are friends.")
print('{} and {} are friends'.format(name,name2))

#printing without newline
print("Peppa", end = ' ')
print('Pig')

print("Hi", end = "")
print("Hello", end = '*')

print()
#taking inputs

var = input('Insert your name: ')
print(var)
var1 = input()
print(var1)
var3 = int(input('Enter a number:'))
print(var3)
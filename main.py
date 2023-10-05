import math

print("Hello Makgabo Mathekga")
first_name = "Makgabo"
last_name = "Mathekga"
full_name = first_name + " " + last_name
print("Hello " + full_name)

age = 32
age += 1
print("Your age is: " + str( age ) )
height = 213.5
print("Your height is: " + str(height) )
print(type(age))
gender = False
print(type(gender))

# how to declare multiple assigments of variables at the same time on the same line:
Spongebob = Patrick = Sam = Squidward = 29
print( str(Spongebob) + ", " + str(Patrick) + ", "  +  str(Sam) + ", "
      +  str(Squidward))

# string methods in Python
print("string methods in Python")
myname = "Makgabo"
print(len(myname))
print(myname.find("a"))
print(myname.capitalize())
print(myname.upper())
print(myname.lower())
print(myname.isdigit())
print(myname.isalpha())
print(myname.count("a"))
print(myname.replace("a", "o"))
print(myname*4) #prints your variables the number of times you multiply it
print("type casting in python")
x = 9
y = 4.5
print( int(y) * x)
print( int(y) )
print("user input in Python")
allnames = input("what are your full names? ")
print("My full names are: " + allnames)
# all input values are string by default, you have to type cats them otherwise
myage = int( input("how old are you"))
myage += 3
print(myage)

print("Math functions")



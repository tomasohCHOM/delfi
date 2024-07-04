# This represents a comment. The purpose of a comment is to express
# your thoughts to potential future code-readers. Anything that goes
# after a "#" is considered a comment in Python. In other programming
# languages (like Java), those may be "//"

print("Hello World!")  # This will print "Hello World!" in the terminal

print("Give me your name:")
name = input()

print("Your name is: " + name)

my_int = int(input("Please pick a number: "))  # int() convers a string to a number
print("Your number is " + str(my_int))  # str() converts to string
print("Your number plus 3 is equal to: " + str(my_int + 3))

# Solution to ask dimensions of a rectangle (width and height)
# Print the area and the perimeter

width = int(input("What is the width of the rectangle? "))
height = int(input("What is the height of the rectangle? "))

print("The area of the rectangle is " + str(width * height))
print("The perimeter of the rectangle is " + str(2 * width + 2 * height))

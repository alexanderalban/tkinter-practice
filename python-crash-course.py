# Working my way through the python crash course book
# Tips and tricks that we'rent in the other book!

# Capitalize names in strings with .title()!

red_ranger = "jason scott"

print(red_ranger.title())

blue_first_name = "billy"
blue_last_name = 'cranston'
blue_full_name = blue_first_name + " " + blue_last_name
print("Hello, " + blue_full_name.title() + "!")

# Adding whitespace with tabs or Newlines
# You can add a tab with \t

print("\tHello, Rangers")

# add a new line with \n
print("Gettings Kimberly, \nTrini, \nZack, \nand Tommy")

# You can also combine these with \n\t

print("Rita is attacking with \n\tGoldar, \n\tBaboo, \n\tand Squatt")

# Stripping white space from strings
# Strip whitespace from the right side of a string

zordoncall = "Rangers! "
print(zordoncall.rstrip())
# This is teporary. to do it permanently you need to store it in the variable:
zordoncall = zordoncall.rstrip()
print(zordoncall)
# Removing from the left side is lstrip, removing from both sides is just strip()

###### More practice!

# Store a person's name as a variable, then print a message to that person
black_ranger = "Zack Taylor"
print("Greetings, " + black_ranger + ".")

# store a name as a variable, then print that name in uppercase, lowercase, and titlecase
pink_ranger = "kimberly hart"
print(pink_ranger.upper())
print(pink_ranger.lower())
print(pink_ranger.title())

# Print a quote from someone you like, include quotation marks
print('\tThe wise Zordon of Eltar once said,\n\t"May the Power Protect You."')

# Same excersize, but store the same as a varable, and the message in a variable called "message"
zordon = "Zordon of Eltar"
message = "\tThe wise " + zordon + ' once said, \n\t"May the Power Protect You."'

print(message)

# Numbers! Here are some number functions that were missed before:
# Python used ** to represent exponents

print(10 * 10)
print(10 ** 10)

# The Zen of Python can be accessed by typing import this

import this
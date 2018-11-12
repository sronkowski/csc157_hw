# ************************************************************************
# * Name: Your name                                                 CSC 157
# * Date: Today's date                                              Lab 4   
# *************************************************************************
# * Statement: Write function printRectangle(base, height, character) that will print
# *	a rectangle made of characters with dimensions base by height 	   	
# * Specifications:
# * Input  - the base, height, and character type
# * Output - the printed rectangle
# ************************************************************************/

# function definition - given the parameters base (int), height (int) and character
# print out a rectangle with dimensions base x height, using the character value
def printRectangle(base, height, character):
	# add the necessary code		
    for h in range(height):
        for b in range(base):
            print(character,sep='',end='')
        print()

#sanitize base value
def checkBase(base):
    while base.isdigit() == False:
        print('\n','The base must be an integer.  Please enter a new base value.')
        base = input('Enter a positive integer for the base of the rectangle: ')
    return int(base)

#sanitize height value
def checkHeight(height):
    while height.isdigit() == False:
        print('\n','The height must be an integer.  Please enter a new height value.')
        height = input('Enter a positive integer for the height of the rectangle: ')
    return int(height)

#sanitize character string
def checkString(character):
    while len(character) != 1:
        print('\n','You may only print a single character.')
        character = str(input('Enter a character used to print the rectangle: '))
    return character

# prompt for input
base = input('Enter a positive integer for the base of the rectangle: ')
height = input('Enter a positive integer for the height of the rectangle: ')
character = str(input('Enter a character used to print the rectangle: '))

#checks that base and height are integers
base = checkBase(base)
height = checkHeight(height)
character = checkString(character)
# print the rectangle by calling the printRectangle function
printRectangle(base, height, character)






 

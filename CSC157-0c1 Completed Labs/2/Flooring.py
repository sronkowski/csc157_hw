# ************************************************************************
# Name: Stephen Ronkowski                                                CSC 155
# Date:9/6/2018                                        Lab 2
# ************************************************************************
# Statement: Determine type of flooring for a new home
# Specifications:
# Input  - Flooring selector
# Output - Appropriate output message based upon selector value
# ************************************************************************

# string literals storing the three options
option1 = '1: Scored concrete, costs $3000.'
option2 = '2: Carpeting comes with a $5000 allowance.'
option3 = ('3: Wood floors in the living area,\ncarpeting in the bed rooms,'
		   'tile in the bath areas,\nand a $5000 carpeting allowance, totaling $10,000.')
option4 = '4: Quit'
# display a descriptive message
print("This program asks a user to enter a choice of flooring for a new home.\n") 



#creating choice variable
choice = 1

#while loop
while choice < 4:

	# display a menu of options for flooring
	print(option1, '\n', option2, '\n', option3, '\n', option4, sep='',end='')
	print('\n')
	# input a choice based upon the menu

	choice = int(input())

	# determine the appropriate output string and display the results

	if choice == 1:
		print('You chose', option1, '\n', '\n', end='')
	elif choice == 2:
		print('You chose', option2, '\n', '\n', end='')
	elif choice == 3:
		print('You chose', option3, '\n', '\n', end='')
	else:
		exit()

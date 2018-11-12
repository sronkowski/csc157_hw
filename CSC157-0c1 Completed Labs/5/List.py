# ************************************************************************
# * Name: Stephen Ronkowski                                                CSC 157
# * Date: 10/26/2018                                             Lab 5
# *************************************************************************
# * Statement: Write the function num_negatives(list) that returns the count of the
# *	number of negative numbers in the list. Write the function negatives(list) that 
# * returns a list containing only the negative numbers. Prompt the user to enter some 
# * numbers and store them in a list. Pass this list in as an argument to the function 
# * numNegatives and print out a description of the correct number of negatives as well 
# * as the list of negative numbers.   	
# * Specifications:
# * Input  - the list
# * Output - the correct count
# ************************************************************************/

# function definition - given the parameter theList, return the count of negative numbers
# in the list
def num_negatives(theList):
    negativeCount = 0
    for i in theList:
        if i < 0:
            negativeCount += 1
    return negativeCount
	
# function definition - given the parameter theList, return a list that contains only 
# the negative numbers in the parameter list 
def negatives(theList):
    negativeList = []
    for i in theList:
        if i < 0:
            negativeList.append(i)
    return negativeList

					


# prompt the user to enter a list of numbers and store them in a list
list = [float(x) for x in input('Enter some numbers separated by whitespace ').split()]

print()    

# output the number of negatives    
print('The number of negatives in the list is', num_negatives(list))

print()

# output the list of negatives numbers    
print('The negatives in the list are ', end = '') 
    
for items in negatives(list):
    print(items, ' ', sep = '', end = '') 
    
print('\n')







 

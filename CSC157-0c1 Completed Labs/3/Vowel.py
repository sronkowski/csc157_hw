# ************************************************************************
# * Name: Your name                                                 CSC 157
# * Date: Today's date                                              Lab 3   
# *************************************************************************
# * Statement: Count the number of occurrences of vowels in an input string
# * Specifications:
# * Input  - search string
# * Output - the string, the count of all characters, and the count of each vowel
# ************************************************************************/

infoString = ('This program asks the user for a sentence,\n'
         'searches the sentence for all vowels,\n'
         'and displays the number of times each vowel appears in the sentence.\n\n')

print(infoString)

# count of the number of a/A occurrences in the sentence
a_count = 0    
# count of the number of e/E occurrences in the sentence
e_count = 0   
# count of the number of i/I occurrences in the sentence      
i_count = 0
# count of the number of o/O occurrences in the sentence         
o_count = 0
# count of the number of u/U occurrences in the sentence        
u_count = 0     
       
# prompt for input    
sentence = input('Enter a sentence: ')

# determine the vowel counts and total character count

	
# display the results	
print('In the sentence', sentence)
for counts in [a_count, e_count, i_count, o_count, u_count]:
    print('there are', counts)




 

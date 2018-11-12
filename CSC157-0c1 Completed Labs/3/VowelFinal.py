# ************************************************************************
# * Name: Stephen Ronkowski                                CSC 157
# * Date: 9/6/2018                                         Lab 3
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

#function to count letters

def count_letter(string, letter):
    count = 0
    for x in string:
        if letter == x:
            count += 1
    return(count)

#count total letters

total_letters = len(sentence)

#use function to count vowels

a_count = count_letter(sentence, 'a') + count_letter(sentence, 'A')

e_count = count_letter(sentence, 'e') + count_letter(sentence, 'E')

i_count = count_letter(sentence, 'i') + count_letter(sentence, 'I')

o_count = count_letter(sentence, 'o') + count_letter(sentence, 'O')

u_count = count_letter(sentence, 'u') + count_letter(sentence, 'U')

# display the results
which_letter = 0

print('The sentence "', sentence,'" has ', total_letters, ' letters and', sep="")
for counts in [a_count, e_count, i_count, o_count, u_count]:
    which_letter += 1
    print('there are', counts, end=' ')
    if which_letter == 1:
        print("a's")
    elif which_letter == 2:
        print("e's")
    elif which_letter == 3:
        print("i's")
    elif which_letter == 4:
        print("o's")
    else:
        print("u's")



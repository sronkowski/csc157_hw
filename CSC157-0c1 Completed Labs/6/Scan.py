# ************************************************************************
# * Name: Your name                                                 CSC 157
# * Date: Today's date                                              Lab 6   
# *************************************************************************
# * Statement: Echos the contents of the file invoice.txt and sums prices and 
# * count of items
# * Specifications:
# * Input  - string describing a tool in the file invoice.txt
# *        - price of the tool in the file invoice.txt
# * Output - Message indicating the item and the cost
# *        - The sum of all costs and the number of items in the file invoice.txt
# ************************************************************************/

# output descriptive messages
print('This program will read each line in the file invoice.txt and print a\n'
       + 'a table indicating the item and it\'s cost.  When the file is exhausted,\n'
       + 'it will print the cumulative sum of all of the costs and the total \n'
       + 'number of items.\n')

invoiceFile = open('invoice.txt', 'r')

#read the raw information from the file and push into a list
def ReadFile(input):
    rawList = []
    line = input.readline()
    while line != '':
        rawList.append(line)
        line = input.readline()
    #oldEnd = rawList[len(rawList)-1]
   # print(oldEnd)
    #newEnd = oldEnd + "\n"
    #rawList.insert([len(rawList)-1], newEnd)
    return rawList

#reads dollar values from main list

def CashFromList(input):
    costList = []
    itemToRead = 0
    while itemToRead < len(input):
        rowToSplit = input[itemToRead]
        loc = rowToSplit.find('#')
        costList.append(rowToSplit[loc+1:].rstrip('\n'))
        itemToRead += 1
    return costList

#prints list in table format
def PrintList(input):
    itemToRead = 0
    while itemToRead < len(input):
        rowToPrint = input[itemToRead].rstrip('\n')
        loc = rowToPrint.find('#')
        print('{:21}'.format(rowToPrint[:loc]), end='')
        print('{:1}'.format('$'),end='')
        print('{:>5}'.format(rowToPrint[loc+1:]))
        itemToRead += 1
    print("\n")

#adds values for total
def AddList(input):
    floatList = []
    for item in input:
        floatList.append(float(item))
    return sum(floatList)

#run the numbers
listFromFile = ReadFile(invoiceFile)
rawCostOfItems = CashFromList(listFromFile)
totalCost = AddList(rawCostOfItems)
# display header line for items list
print('{0: <10}'.format('Item'), '{0: >17}'.format('Cost'), sep = '' )
PrintList(listFromFile)
print('{:21}'.format("Total cost"), end='')
print('{:1}'.format('$'),end='')
print('{:>5,.2f}'.format(totalCost))

print('{:21}'.format("Number of tools"), end='')
print('{:>6}'.format(len(rawCostOfItems)))


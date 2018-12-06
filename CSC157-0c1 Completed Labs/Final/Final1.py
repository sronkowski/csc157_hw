#main menu
import pandas as pd
import numpy as np
def main():
    print('(1) EXPANDED SUM','(2) REVERSE EXPANDED SUM','(3) REVERSE INTEGER','(4) PRODUCT TABLE', '(5) EXIT', sep ='\n')
    menuChoice = input('Choose an option:')

    if menuChoice == '1':
        numberToProcess = promptForNumber()
        printSum(numberToProcess, False)
    elif menuChoice == '2':
        numberToProcess = promptForNumber()
        printSum(numberToProcess, True)
    elif menuChoice == '3':
        numberToProcess = promptForNumber()
        print('The positive integer you entered, reversed is', reverseInt(numberToProcess), '\n')
    elif menuChoice == '4':
        numberToProcess = promptForNumber()
        print('\n')
        printProductTable(numberToProcess)
    elif menuChoice == '5':
        quit()
    else:
        print('Invalid selection.  Try again.', '\n')
    main()


def printProductTable(n):
    #define variables for processing.
    rowNameList = []
    columnNameList = []
    listOfInts = np.arange(1,(n+1), 1)
    rowDim = 0
    columnDim = 0
    letterNum = int(65)

    #Generate row names
    while rowDim < n:
        rowNameList.append(str(rowDim + 1))
        rowDim += 1
    rowNameList = [n + '|' for n in rowNameList]

    #Generate column names
    while columnDim < n:
        columnNameList.append(chr(letterNum))
        letterNum += 1
        columnDim += 1

    #Generate list of products.
    rowDim = 1
    listToPrint = []
    while rowDim <= columnDim:
        listToPrint.append(listOfInts * rowDim)
        rowDim += 1

    #Convert list to pandas DataFrame for ease of formatting.
    finalOutput = pd.DataFrame(listToPrint, index = rowNameList, columns = columnNameList)


    print(finalOutput, '\n')



#sanitize input number before processing through appropriate function
def checkIfNumber(number):
    #first, check to see if the value can be converted into a float.
    try:
        float(number)
    except ValueError:
        print('You may only select an positive integer, and your value was not a number.  Try again.')
        return False
    return True


 #now, check to see if it is an integer, and then check to see if it is positive.
def checkIfInteger(number):
    if float(number) % 1 != 0:
        print('You may only select an positive integer, and your value was not an integer.  Try again.')
        promptForNumber()
    elif int(number) <= 0:
        print('You may only select a positive integer, and your value was negative. Try again.')
        promptForNumber()
    else:
        pass

#function to call at start of each menu option. Takes no inputs, outputs int.
def promptForNumber():
    numberChoice = input('Enter a positive integer:')
    if checkIfNumber(numberChoice) == True:
        checkIfInteger(numberChoice)
    else:
        promptForNumber()
    numberChoice = int(numberChoice)
    return numberChoice

#function to reverse an integer string.
def reverseInt(n):
    output = ''
    n = str(n)
    for char in n:
        output = char + output
    output = int(output)
    return output

def printSum(n, reverse):
    plusCount = n - 1
    if reverse == True:
        nPrint = n
        while nPrint > 0:
            print(nPrint, sep='', end='')
            nPrint -= 1
            if plusCount > 0:
                print('+', sep='', end='')
                plusCount -= 1
            else:
                pass
    else:
        nPrint = 1
        while nPrint <= n:
            print(nPrint, sep='', end='')
            nPrint += 1
            if plusCount > 0:
                print('+', sep='', end='')
                plusCount -= 1
            else:
                pass
    print('=', sum(n), '\n', sep='')

def sum(n):
    sum = 0
    while n > 0:
        sum = n + sum
        n -= 1
    return sum

main()

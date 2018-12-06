"""
Variables:

Book - Title, Author, Patron who Has It, Wait List x3
Patron - Name, number of books checked out

"""
import pandas as pd

def firstboot():
    #test to see if database files exist - if not, create blank versions.
    try:
        test1 = open('book.csv')
    except:
        print('No book file found - creating empty file.')
        initDB1 = pd.DataFrame(columns=['Title', 'Author', 'Current Holder', 'Waitlist 1', 'Waitlist 2', 'Waitlist 3'])
        initDB1.to_csv('book.csv', index=False)
    try:
        test2 = open('patron.csv')
    except:
        print('No patron file found - creating empty file.')
        initDB2 = pd.DataFrame(columns=['Name', 'Number of Books'])
        initDB2.to_csv('patron.csv', index=False)


class Book:

    def __init__(self, bookname):
        self.bookDB = pd.read_csv('book.csv')

        if bookname == 'skipload':
            self.printlist = self.bookDB[['Title', 'Author', 'Current Holder']]
            self.waitlist = self.bookDB[['Title', 'Waitlist 1', 'Waitlist 2', 'Waitlist 3']]
        else:
            self.bookname = bookname
            try:
                self.indexLocation = self.bookDB[self.bookDB['Title'] == self.bookname].index.values.astype(int)[0]
                self.author = self.bookDB.loc[self.bookDB['Title'] == self.bookname]['Author'].values.astype(str)[0]
                self.holder = self.bookDB.loc[self.bookDB['Title'] == self.bookname]['Current Holder'].values.astype(str)[0]
                self.wait1 = self.bookDB.loc[self.bookDB['Title'] == self.bookname]['Waitlist 1'].values.astype(str)[0]
                self.wait2 = self.bookDB.loc[self.bookDB['Title'] == self.bookname]['Waitlist 2'].values.astype(str)[0]
                self.wait3 = self.bookDB.loc[self.bookDB['Title'] == self.bookname]['Waitlist 3'].values.astype(str)[0]
            except:
                print('The book name you entered could not be located in the database - please check your spelling and confirm the book is in database.  Returning to book menu...')
                bookmenu()

    def exists(self):
        pass

    def isCheckedOut(self):
        if self.holder == 'none':
            return False
        else:
            return True

    def checkout(self, patron):
       #update record
        self.bookDB.loc[self.indexLocation] = [self.bookname, self.author, patron, self.wait1, self.wait2, self.wait3]
        print(patron,"has checked out",self.bookname,".")
        print("Saving book database...")
        self.bookDB.to_csv('book.csv', index = False)

    def returned(self):
        #update database listing.
        self.bookDB.loc[self.indexLocation] = [self.bookname, self.author, 'none', self.wait1, self.wait2, self.wait3]
        #print waitlist status
        if self.wait1 != 'none':
            print(self.wait1, " is the next person on the waitlist - please notify them that the book is available.")
        else:
            print("There is nobody on the waitlist for this book.")
        #save database
        self.bookDB.to_csv('book.csv', index=False)
        print(self.holder,'has been marked as returning',self.bookname)
        #update patron record
        Patron(self.holder).returned()

    def waitlistbypatron(self, name):
        try:
            firstspot = self.waitlist.loc[self.waitlist['Waitlist 1'] == name]['Title'].values.astype(str)[0]
        except:
            firstspot = 'none'
        try:
            secondspot = self.waitlist.loc[self.waitlist['Waitlist 2'] == name]['Title'].values.astype(str)[0]
        except:
            secondspot = 'none'
        try:
            thirdspot = self.waitlist.loc[self.waitlist['Waitlist 3'] == name]['Title'].values.astype(str)[0]
        except:
            thirdspot = 'none'

        print()
        print(name,'is currently first on the waitlist for:')
        print(firstspot)
        print(name, 'is currently second on the waitlist for:')
        print(secondspot)
        print(name, 'is currently third on the waitlist for:')
        print(thirdspot)


    def list(self):
        return self.printlist

    def findbypatron(self,patron):
                return self.printlist.loc[self.printlist['Current Holder'] == patron]['Title']


    def add(self, title, author):
        self.bookDB.index = self.bookDB.index + 1
        self.bookDB.loc[0] = [title, author, 'none', 'none', 'none', 'none']
        self.bookDB = self.bookDB.sort_index()
        self.bookDB.to_csv('book.csv', index=False)


    def waitlist(self, name):
        if self.holder == 'none' and self.wait1 == 'none':
            print("Alert - this book is currently not checked out and there is no waitlist.", name,'will be added to Waitlist, but book can be checked out using Check Out from Waitlist option.')
        else:
            pass

        if self.wait1 == 'none':
            self.bookDB.loc[self.indexLocation] = [self.bookname, self.author, self.holder, name, 'none',
                                               'none']
            self.bookDB.to_csv('book.csv', index=False)
        elif self.wait2 == 'none':
            self.bookDB.loc[self.indexLocation] = [self.bookname, self.author, self.holder, self.wait1, name,
                                                   'none']
            self.bookDB.to_csv('book.csv', index=False)

        elif self.wait3 == 'none':
            self.bookDB.loc[self.indexLocation] = [self.bookname, self.author, self.holder, self.wait1, self.wait2,
                                                   self.wait3]
            self.bookDB.to_csv('book.csv', index=False)
        else:
            print("Error - no more than three patrons can be on the waitlist for a book - returning to book menu.")

    def checkfromwaitlist(self):
        if self.holder != 'none':
            print('Alert -',self.bookname,'is currently checked out to',self.holder,', so this operation cannot be continued.  Returning to book menu...')
            bookmenu()
        else:
            pass

        if Patron(self.wait1).countInt() > 2:
            print('Alert -',self.wait1,'is currently first on the waitlist, but this patron already has three books checked out. Please notify the patron that they must return a book before checking out this title.')
            print('Returning to Book Menu.')
            bookmenu()
        else:
            print(self.wait1,'is currently first on the waitlist - press \'y\' to check out book to this patron, or press any other key to exit.')
            check = input('')
            if check == 'y':
                self.bookDB.loc[self.indexLocation] = [self.bookname, self.author, self.wait1, self.wait2, self.wait3,
                                                   'none']
                Patron(self.wait1).checkout(self.bookname)
                self.bookDB.to_csv('book.csv', index=False)
            else:
                pass

class Patron:
    def __init__(self, name):
        self.name = name
        self.patronDB = pd.read_csv('patron.csv')

        if name == 'skipload':
            self.printDB = self.patronDB
        else:
            try:
                self.indexLocation = self.patronDB[self.patronDB['Name'] == name].index.values.astype(int)[0]
                self.currentCount = int(self.patronDB.loc[self.patronDB['Name'] == name]['Number of Books'])
            except:
                print('The patron name you entered could not be located in the database - please check your spelling and confirm the patron is in the database.  Returning to patron menu...')
                patronmenu()

    def exists(self):
        pass

    def addpatron(self, name):
        self.patronDB.index = self.patronDB.index + 1
        self.patronDB.loc[0] = [name, 0]
        self.patronDB = self.patronDB.sort_index()
        print('Patron added successfully! Saving database.')
        self.patronDB.to_csv('patron.csv', index=False)

    def countInt(self):
        return int(self.currentCount)

    def returned(self):
        self.currentCount -= 1
        self.patronDB.loc[self.indexLocation] = [self.name, self.currentCount]
        print('Updating patron database...')
        self.patronDB.to_csv('patron.csv', index=False)

    def checkout(self, bookname):
        if Book(bookname).isCheckedOut() == False:
            pass
        else:
            print()
            print('Error - this book is currently checked out!  Returning to book menu.')
            bookmenu()

        if self.currentCount < 3:
            self.currentCount += 1
            self.patronDB.loc[self.indexLocation] = [self.name, self.currentCount]
            print("Saving patron database...")
            self.patronDB.to_csv('patron.csv', index=False)
            Book(bookname).checkout(self.name)
        else:
            print("The patron already has three books checked out - they can't check out any more!")


    def printlist(self):
        return self.currentCount

    def list(self):
        print(self.printDB)

def main():
    print()
    print('Main Menu:', '1. Book Database', '2. Patron Database', '3. Exit.',sep = '\n')
    print()
    menuChoice = input('Make a selection.')

    if menuChoice == '1':
        bookmenu()
    elif menuChoice == '2':
        patronmenu()
    elif menuChoice == '3':
        quit()
    else:
        print('Invalid selection.  Try again.', '\n')
    main()

def bookmenu():
    print()
    print('Book Menu:', '1. Check Out Book', '2. Return Book', '3. Add Patron to Book Waitlist', '4. Check Out Book to Waitlisted Patron', '5. List Books.', '6. Add Book.', '7. Return to Main Menu.',sep = '\n')
    print()
    menuChoice = input('Make a selection.')

    if menuChoice == '1':
        book = input("What is the title of the book to be checked out?")
        name = input("What is the name of the person checking out the book?")
        Book(book).exists()
        Patron(name).checkout(book)

    elif menuChoice == '2':
        book = input("What is the title of the book to be returned?")
        Book(book).returned()

    elif menuChoice == '3':
        book = input("What title would you like to add a waitlist entry to?")
        name = input("What is the name of the person to add?")
        Patron(name).exists()
        Book(book).waitlist(name)

    elif menuChoice == '4':
        book = input("What title would you like to check out to the first waitlisted patron?")
        print()
        Book(book).checkfromwaitlist()

    elif menuChoice == '5':
        print()
        print(Book('skipload').list())

    elif menuChoice == '6':
        book = input("What is the title of the book to be added?")
        author = input("Who is the author?")
        Book('skipload').add(book, author)

    elif menuChoice == '7':
        main()

    else:
        print('Invalid selection.  Try again.', '\n')
    bookmenu()


def patronmenu():
    print()
    print('Patron Menu:', '1. Number of Books by Patron', '2. Books Checked out By Patron.', '3. Waitlist by Patron.', '4. Add Patron.', '5. List Patrons.',
          '6. Return to Main Menu.', sep = '\n')
    print()
    menuChoice = input('Make a selection.')

    if menuChoice == '1':
        nametofind = input("Who would you like to get the total number of books checked out for?")
        print()
        print(nametofind, 'currently has', Patron(nametofind).printlist(),'book(s) checked out.')

    elif menuChoice == '2':
        nametofind = input("Who would you like to get the books checked out for?")
        Patron(nametofind).exists()
        print()
        print(Book('skipload').findbypatron(nametofind))

    elif menuChoice == '3':
        nametofind = input("Who would you like to get a waitlist readout for?")
        print()
        Book('skipload').waitlistbypatron(nametofind)

    elif menuChoice == '4':
        nametoadd = input("Who would you like to add?")
        print()
        Patron('skipload').addpatron(nametoadd)

    elif menuChoice == '5':
        Patron('skipload').list()

    elif menuChoice == '6':
        main()

    else:
        print('Invalid selection.  Try again.', '\n')

    patronmenu()

firstboot()
main()
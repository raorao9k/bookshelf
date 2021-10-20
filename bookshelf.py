'''
    File Name:  bookshelf.py
    Author:     Akshay Rao
    Date:       October 20, 2021
    Modified:   None
    Copyright Akshay Rao 2021
'''

import csv

filename = "bookshelf.csv"
headers = ["TITLE",
          "LAST NAME",
          "FIRST NAME",
          "SHELF",
          "SECTION",
          "FORMAT",
          "GENRE",
          "SERIES",
          "SERIES#",
          "NOTES"]
entry = ["", "", "", "", "", "", "", "", "", ""]
shelves = ["Abandoned",
           "Gift",
           "Potential",
           "Read",
           "Reading",
           "Recommended",
           "Purchased",
           "To Gift",
           "To Listen",
           "To Read"]
sections = ["9-12",
            "Kids",
            "Fiction",
            "Non-fiction",
            "Teen",
            "Well-being"]
formats = ["Audiobook",
           "Ebook",
           "Hardcover",
           "Paperback"]
genres = ["Classic",
          "Crime",
          "Fantasy",
          "Historical",
          "Horror",
          "Memoir",
          "Mystery",
          "Puzzles",
          "Romance",
          "Sci-fi",
          "Self Help"
          "Thriller",
          "Western"]

def main():
    '''
        Run a continuous loop until user exits with keyboard input.
    '''

    userInterface()

def printAllSeries():
    '''
        Iterate through csv file and print header row and all rows in which "SERIES" is not an empty string.
    '''
    count = 1
    print("******************************************************************************************************************************************************")
    with open(filename) as file:
            data = csv.reader(file)
            for row in data:
                if row[7] != '':
                    print('{:<25} {:<45} {:<9} {:<13} {:<35}'.format(row[7],row[0],row[8],row[3],row[9]))
                    if count == 1:
                        print("******************************************************************************************************************************************************")
                        count = count + 1

def userInterface():
    '''
        Print program options for the user and collect the user's option. Repeat until the user inputs the option to exit the program.
    '''
    print("****************************************************************************************************************************************************************************************")
    print("*** Akshay's Bookshelf *****************************************************************************************************************************************************************")
    print("****************************************************************************************************************************************************************************************")

    option = '0'

    while (option != '9'):
        print("\n")
        print("1 - Add book\n")
        print("2 - Remove book\n")
        print("3 - Find book by title\n")
        print("4 - Find books by author last name\n")
        print("5 - Find books by shelf\n")
        print("6 - Move book to another shelf\n")
        print("7 - List all books\n")
        print("8 - List all series\n")
        print("9 - Exit program\n\n")

        option = input("What do? ")
        print("****************************************************************************************************************************************************************************************")
        
        if option == '1':
            addBook()
        elif option == '2':
            removeBook()
        elif option == '3':
            listBy(1)
        elif option == '4':
            listBy(2)
        elif option == '5':
            listBy(4)
        elif option == '6':
            changeShelf()
        elif option == '7':
            listBy(0)
        elif option == '8':
            printAllSeries()
        elif option == '9':
            break
        else:
            print("Invalid option. Select again.\n")

        print("****************************************************************************************************************************************************************************************")

def createFile(fname):
    ''' (str) ->
        Create a csv file with name 'fname'. Write each item in the list 'headers' to the csv file in one row.
    '''
    
    file = open(fname, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(header)
    file.close()

def addBook():
    '''
        Take input strings from user for a new entry append the entry to the csv file.
    '''

    global headers
    global entry

    count = 0
    myEntry = ""
    for x in headers:
        myEntry = input(x+": ")
        entry[count] = myEntry
        count = count + 1

    with open(filename, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(entry)

def removeBook():
    '''
        Collect and store book title from user. Find and remove book from csv file.        
    '''

    title = input("Book Title: ")
    myData = []
    
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            myData.append(row)
            if row[0] == title:
                myData.pop()

    with open(filename, 'w') as file:
        data = csv.writer(file)
        data.writerows(myData)

def listBy(index):
    ''' (int) ->
        'index' determines whether to search the csv file by title, author, or status.
            0 - List all
                    Read all books from csv file and print to terminal row by row with formatting.
            1 - By title
            2 - By author last name
            3 - By author first name
            4 - By shelf
    '''

    key = "myKey"
    count = 0
    
    if index == 0:
        key = "all" 
    elif index == 1:
        key = input("Book Title: ")
    elif index == 2:
        key = input("Author Last Name: ")
    elif index == 3:
        key = input("Author First Name: ")
    elif index == 4:
        key = input("Book Shelf: ")
    else:
        key = "error"
    
    if index == 0:
        with open(filename) as file:
            data = csv.reader(file)
            for row in data:
                if count == 1:
                    print("****************************************************************************************************************************************************************************************")
                print('{:<50} {:<20} {:<20} {:<15} {:<30} {:<35}'.format(row[0],row[1],row[2],row[3],row[7],row[9]))
                count = count + 1
    else:
        print("****************************************************************************************************************************************************************************************")
        with open(filename) as file:
            data = csv.reader(file)
            for row in data:
                if count == 0:
                    print('{:<50} {:<20} {:<20} {:<15} {:<30} {:<35}'.format(row[0],row[1],row[2],row[3],row[7],row[9]))
                    print("****************************************************************************************************************************************************************************************")                 
                if row[index-1] == key:
                    print('{:<50} {:<20} {:<20} {:<15} {:<30} {:<35}'.format(row[0],row[1],row[2],row[3],row[7],row[9]))
                count = count + 1


def changeShelf():
    '''
        Collect and store existing book title and its new status from the user.
        Search csv file using the book title and store all book info in 'myRow'.
        Write new status to 'myRow' and open csv file to replace the row entry
        of the book.
    '''

    title = input("Book Title: ")
    shelf = input("New Shelf: ")

    myRow = []
    myData = []
    flag = 0
    
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            if row[0] == title:
                myRow = row
                myRow[3] = shelf
                myData.append(myRow)
            else:
                myData.append(row)

    with open(filename, 'w') as file:
        data = csv.writer(file)
        data.writerows(myData)

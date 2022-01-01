'''
    File Name:  bookshelf.py
    Author:     Akshay Rao
    Date:       January 1, 2022
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
           "Potential",
           "Read",
           "Reading",
           "Recommended",
           "Purchased",
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
    ''' (NoneType) -> NoneType
        Call the user interface function.
    '''

    userInterface()

def printAllSeries():
    ''' (NoneType) -> NoneType
        Iterate through the csv file and print header row and all rows in which "SERIES" is not an empty string.
    '''
    count = 1
    print("*****************************************************************************************************************************************************************************************************")
    with open(filename) as file:
            data = csv.reader(file)
            for row in data:
                if row[7] != '':
                    print('{:<35} {:<45} {:<9} {:<13} {:<35}'.format(row[7],row[0],row[8],row[3],row[9]))
                    if count == 1:
                        print("*****************************************************************************************************************************************************************************************************")
                        count = count + 1

def userInterface():
    ''' (NoneType) -> NoneType
        Print program options for the user and collect the user's option. Repeat until the user inputs the option to exit the program.
    '''
    print("*****************************************************************************************************************************************************************************************************")
    print("*** Akshay's Bookshelf ******************************************************************************************************************************************************************************")
    print("*****************************************************************************************************************************************************************************************************")

    option = '0'
    searchResults = []

    while (option != '6'):
        print("\n")
        print("1 - Add book\n")
        print("2 - Remove book\n")
        print("3 - Find book\n")
        print("4 - Move book to another shelf\n")
        print("5 - List all series\n")
        print("6 - Exit program\n\n")

        option = input("What do? ")
        print("*****************************************************************************************************************************************************************************************************")
        
        if option == '1':
            addBook()
        elif option == '2':
            removeBook()
        elif option == '3':
            searchResults = searchFile()
            printBooks(searchResults)
        elif option == '4':
            changeShelf()
        elif option == '5':
            printAllSeries()
        elif option == '6':
            break
        else:
            print("Invalid option. Select again.\n")

        print("*****************************************************************************************************************************************************************************************************")

def createFile(fname):
    ''' (str) -> NoneType
        Create a csv file with name fname. Write each item in the global list headers to the csv file in one row.
    '''
    
    file = open(fname, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(header)
    file.close()

def addBook():
    ''' (NoneType) -> NoneType
        Take input strings from the user for a new entry and append the entry to the csv file.
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
    ''' (NoneType) -> NoneType
        Collect and store the book title from user. Find and remove the book from the csv file.        
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

def searchFile():
    ''' (NoneType) -> list of [str]
        Take user input for the search term. Search the csv file row by row for the keyword. If found, append the row as an item in myResults.
        Return myResults.
    '''

    count = 0
    myResults = []
    myEntry = input("Search term: ")

    print("*****************************************************************************************************************************************************************************************************")

    with open(filename) as file:
            data = csv.reader(file)
            for row in data:
                for x in row:
                    if (myEntry in x) and count == 0:
                        myResults.append(row)
                        count = count + 1
                count = 0
    return myResults

def printBooks(myBooks):
    ''' (list of list) -> NoneType
        Print headers and all items in myBooks to screen.
    '''

    print('{:<50} {:<35} {:<15} {:<12} {:<30} {:<35}'.format(headers[0],headers[1],headers[2],headers[3],headers[7],headers[9]))    
    print("*****************************************************************************************************************************************************************************************************")
    for book in myBooks:
        print('{:<50} {:<35} {:<15} {:<12} {:<30} {:<35}'.format(book[0],book[1],book[2],book[3],book[7],book[9]))
    
def changeShelf():
    ''' (NoneType) -> NoneType
        Collect and store existing book title and its new status from the user. Search csv file using the book title and store all book info in 'myRow'.
        Write new status to myRow and open csv file to replace the row entry of the book.
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

def updateBook(myBook):
    ''' (list) -> (list)
        Prompt the user to update any field in myBook, update it, and return the updated myBook.
    '''

    myNewBook = myBook
    count = 0
    myField = ""
    myValue = ""    

    myField = input("Which field to be changed? ")

    count = 0
    if myField.lower() == "all":
        for field in myBook:
            myNewBook[count] = input("{0}: ".format(headers[count]))
            count = count + 1
    else:
        for field in headers:
            if myField.lower() == headers[count].lower():
                myValue = input("Enter new {0}: ".format(myField.lower()))
                myNewBook[count] = myValue
            count = count + 1

    print("")            

    return myNewBook

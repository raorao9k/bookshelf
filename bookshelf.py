'''
    File Name:  bookshelf.py
    Author:     Akshay Rao
    Date:       September 18, 2021
    Modified:   None
    Copyright Akshay Rao, 2021
'''

import csv

filename = "bookshelf.csv"
header = ("TITLE", "AUTHOR", "STATUS")

def main():
    '''
        Print program options for the user and collect the user's option.
        Repeat until the user inputs the option to exit the program.
    '''

    'createFile()'

    print("\n************************************************************************************")
    print("**** Akshay's Bookshelf ************************************************************")
    print("************************************************************************************")

    option = '0'

    while (option != '4'):
        print("\n")
        print("1 - Add book\n")
        print("2 - Update book status\n")
        print("3 - List all books\n")
        print("4 - Exit program\n\n")

        option = input("What do? ")
        print("\n************************************************************************************")
        
        if option == '1':
            addBook()
        elif option == '2':
            updateBookShelf()
        elif option == '3':
            listBooks()
        elif option == '4':
            break
        else:
            print("Invalid option. Select again.\n")


def createFile():
    ''' 
        Create a csv file with name 'filename' if it does not exist in
        the root directory.
    '''
    
    file = open(filename, 'w', newline='')
    print(file)
    writer = csv.writer(file)
    writer.writerow(header)
    file.close()

def addBook():
    '''
        Collect and store new book info from user: title, author, status.
        Append new book to csv file.
    '''
       
    title = input("Book Title: ")
    author = input("Book Author: ")
    status = input("Book Status: ")

    with open(filename, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title,author,status])

def listBooks():
    '''
        Read all books from csv file and print to terminal row by row
        with formatting.
    '''

    count = 0
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            if count == 1:
                print("************************************************************************************")
            print('{:<35} {:<25} {:<25}'.format(*row))
            count = count + 1
    print("************************************************************************************")

def updateBookShelf():
    '''
        Collect and store existing book title and its new status from the user.
        Search csv file using the book title and store all book info in 'myRow'.
        Write new status to 'myRow' and open csv file to replace the row entry
        of the book.
    '''

    title = input("Book Title: ")
    status = input("New Status: ")

    myRow = []
    myData = []
    line = 0
    
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            myData.append(row)
            if row[0] == title:
                myRow = row
                myRow[2] = status
                break
            line = line + 1

    with open(filename, 'w') as file:
        data = csv.writer(file)
        data.writerows(myData)

'''
    File Name:  bookshelf.py
    Author:     Akshay Rao
    Date:       September 22, 2021
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
    print("* Akshay's Bookshelf ***************************************************************")
    print("************************************************************************************")

    option = '0'

    while (option != '8'):
        print("\n")
        print("1 - Add book\n")
        print("2 - Remove book\n")
        print("3 - Find book\n")
        print("4 - Find author\n")
        print("5 - Find status\n")
        print("6 - Update status\n")
        print("7 - List all books\n")
        print("8 - Exit program\n\n")

        option = input("What do? ")
        print("\n************************************************************************************")
        
        if option == '1':
            addBook()
        elif option == '2':
            removeBook()
        elif option == '3':
            findBy(0)
        elif option == '4':
            findBy(1)
        elif option == '5':
            findBy(2)
        elif option == '6':
            newStatus()
        elif option == '7':
            listAllBooks()
        elif option == '8':
            break
        else:
            print("Invalid option. Select again.\n")

        print("************************************************************************************")

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

def removeBook():
    '''
        Collect and store book title from user. Find and remove book from
        csv file.        
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

def findBy(index):
    ''' (int) ->
        'index' determines whether to search the csv file by title, author, or status.
            0 - By title
            1 - By author
            2 - By status
    '''

    key = "myKey"
    if index == 0:
        key = input("Book Title: ")
    elif index == 1:
        key = input("Author: ")
    elif index == 2:
        key = input("Book Status: ")
    else:
        print("ERRORRRRRR!")
    print("************************************************************************************")

    count = 0
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            if count == 0 or row[index] == key:
                print('{:<45} {:<25} {:<25}'.format(*row))
            if count == 1:
                print("************************************************************************************")
            count = count + 1

def newStatus():
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
    flag = 0
    
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            if row[0] == title:
                myRow = row
                myRow[2] = status
                myData.append(myRow)
                flag = 1
                break
            if flag == 0:
                myData.append(row)

    with open(filename, 'w') as file:
        data = csv.writer(file)
        data.writerows(myData)

def listAllBooks():
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
            print('{:<45} {:<25} {:<25}'.format(*row))
            count = count + 1
    print("************************************************************************************")

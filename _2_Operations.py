from _1_Book_Details import *

class Operation:
    booklist = []

    def addBook(self):
        ID = int(input("Enter the book ID : "))
        name = input("Enter the book name : ")
        edition = input("Enter the book edition : ")
        publisher = input("Enter the publisher name : ")
        price = float(input("Enter the book price : "))
        book_obj = Book(ID = ID, name = name, edition = edition, publisher = publisher, price = price)
        self.booklist.append(book_obj)
        print(f"The book titled {name}, has been added successfully.")

    def viewBook(self):
        for books in self.booklist:
            print(books,'\n')

    def deleteBook(self):
        ID = int(input("Enter the book ID you want to delete : "))
        for books in self.booklist:
            if books.get_ID() == ID:
                self.booklist.remove(books)
                print("The book got deleted successfully.")
                break
        else:
            print("Book is not present in given list.")

    def searchBookByID(self):
        ID = int(input("Enter the book ID you are looking for : "))
        for books in self.booklist:
            if books.get_ID() == ID:
                print(books)
                break
        else:
            print("The mentioned book ID is not present in list.")

    def searchBookByName(self):
        name = input("Enter the book name you are looking for : ")
        for books in self.booklist:
            if books.get_name() == name:
                print(books)
                break
        else:
            print("The mentioned book ID is not present in list.")

    def updateBook(self):
        ID = int(input("Enter the ID to be updated : "))
        for books in self.booklist:
            if books.get_ID() == ID:
                name = input("Enter the book name : ")
                edition = input("Enter the book edition : ")
                publisher = input("Enter the publisher name : ")
                price = float(input("Enter the book price : "))
                books.set_name(name)
                books.set_edition(edition)
                books.set_publisher(publisher)
                books.set_price(price)
                break
        else:
            print("The mentioned book ID is not present in list.")
                



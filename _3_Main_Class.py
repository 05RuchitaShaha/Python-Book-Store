## when MAIN class is called, exceute() will run & whatever present inside it will get executed

from _2_Operations import *

class Main:
    def execute(self,choice,operation):
        if choice == 1:
            print("***Add Book***")
            operation.addBook()
        
        if choice == 2:
            print("***View Books***")
            operation.viewBook()

        if choice == 3:
            print("***Delete Book***")
            operation.deleteBook()

        if choice == 4:
            print("***Search Book by ID***")
            operation.searchBookByID()

        if choice == 5:
            print("***Search Book by Name***")
            operation.searchBookByName()

        if choice == 6:
            print("***Update Book***")
            operation.updateBook()



if __name__ == "__main__":    # driver to drive the code
    operation = Operation()     # create obj for Operation & Main class
    main = Main() 
    while True:
        choice = int(input("Enter \n1.Add Book \n2.View Book \n3.Delete Book \n4.Search Book by ID \n5.Search Book by Name \n6.Update Book \n"))
        main.execute(choice,operation)



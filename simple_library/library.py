#Library class to store info about books, lend a book, add a book, return a book
class Library:
    #Constructor to initialize the book list and a dictionary to keep record of books that are lended
    def __init__(self, list):
        self.booksList = list
        self.lend = {}
    

    #Fuction to display the books present in the books list
    def displayBooks(self):
        print(f"\nBooks available: ")
        for book in self.booksList:
            print(book)


    #Function to lend the book only if the books is not in use by another user.
    def lendBook(self, user, book):
        #check if the book requested is used by another user or not
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print("Books dictionary has been updated")
        else:
            print(f"Books is already being used by {self.lend[book]}")


    #Function to add a book to the book list
    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to books list")
    

    #Function to return a book that is lended by an user.
    def returnBook(self, book):
        self.lend.pop(book)



if __name__ == "__main__":
    lib = Library(['Statistics-II', 'CPP', 'Numerical Method', 'Data Structures and Algorithms', 'Digital Logic'])
    print("\t\t\t\tWelcome to our Library.")
    while(True):
        print("\nEnter your choice to continue")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice = input("Your choice: ")

        #Check if the input is valid or not
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)


        #Perform operations based on the user input
        if user_choice == 1:
            lib.displayBooks()

        elif user_choice == 2:
            book = input("Enter the book you want to Lend: ")
            user = input("Enter your name: ")
            lib.lendBook(user,book)

        elif user_choice == 3:
            book = input("Enter the book you want to Add: ")
            lib.addBook(book)
            
        elif user_choice == 4:
            book = input("Enter the book you want to Return: ")
            lib.returnBook(book)
        else:
            print("Invalid option")

        choice = input("Do you want to conintue(y/n): ")
        if(choice == 'y'):
            continue
        elif(choice == 'n'):
            exit()
        else:
            print("Invalid choice")

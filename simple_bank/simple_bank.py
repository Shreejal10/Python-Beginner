# Parent Class
# Contains user details: name, age gender
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showDetails(self):
        print("\t\t\t\tUser Details")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


# Cild class
# inherits User class along with providing functions for deposit, withdraw and view current balance
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def depositMoney(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(
            f"Rs.{self.amount} deposited successfully. Your new balance is Rs {self.balance}")

    def withdrawMoney(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(
                f"Insufficeint fund in your account. Available balance is Rs {self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(
                f"Rs.{self.amount} withdrawn. Your new balance is Rs {self.balance}")

    def viewBalance(self):
        print(f"Your balance is Rs {self.balance}")


print("\t\t\t\tWelcome to your Bank!!!!!")
# initialize a user by getting inputs
name = input("Enter your Name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
user = Bank(name, age, gender)  # create an object for class Bank


ch = True  # initialize conditon for do-while loop
while ch:
    print("\nPlease select a option for what would to like to do:")
    print("1. View Your Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Balance")
    choice = input("Your Choice: ")
    print()
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            user.showDetails()

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            user.depositMoney(amount)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            user.withdrawMoney(amount)

        elif choice == 4:
            user.viewBalance()

        else:
            print("Invalid number entered")
    else:
        print("Please enter a valid number again")

    c = input("\nDo you want to perform another operation (y/n): ")
    if c == 'y':
        ch = True
    elif c == 'n':
        ch = False
    else:
        print("Invalid option")
        ch = False
        break

print("\n\n\n\t\t\t\tThank you for using our bank: ")
a = input("Enter any key to exit: ")

import string
import random
import time


lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

password_length = input("Enter the length of password required: ")


if password_length.isdigit(): #check is the input is a number or not
    password_length = int(password_length)
    password = [] #create a empty list

    #add the variables to the list
    password.extend(list(lower_case))
    password.extend(list(upper_case))
    password.extend(list(digits))
    password.extend(list(punctuation))
    print("Randomly generated password: " + "".join(random.sample(password, password_length)))
    input("Enter any key to exit: ")

else:
    print("Enter a valid number!")
    time.sleep(2)
    exit()


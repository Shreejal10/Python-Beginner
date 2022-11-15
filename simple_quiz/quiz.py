# Simple quiz game
import time
print("\n\t\t\tWelcome to the quiz game !!!!!!")

# ask if the user want to play the game or not
ch = input("\nDo you want to play the game?(y/n): ")
if ch != 'y':  # if the user doesnt want to play the game exit the user.
    print("Feels bad to see you go.")
    time.sleep(2)
    exit()

# initialize the initial value for possible answers: right, wrong or invalid input
correct_ans = 0
wrong_ans = 0
invalid_ans = 0


# question 1
def ques1():
    global correct_ans
    global wrong_ans
    global invalid_ans
    print("\n1. What is the full form of RAM ?")
    print("\ta. Random Access Memory  \tb. Ram Access Memory \n\tc. Random Acess Memory  \td. Random Accessing Memory")
    ans = input("   Enter your choice: ")
    if ans == 'a':
        correct_ans = correct_ans + 1
    elif ans == 'b' or ans == 'c' or ans == 'd':
        wrong_ans += 1
    else:
        invalid_ans += 1


# question 2
def ques2():
    global correct_ans
    global wrong_ans
    global invalid_ans
    print("\n2. Which is the only country that has a triangular flag ?")
    print("\ta. Mexico  \tb. UAE \n\tc. India  \td. Nepal")
    ans = input("   Enter your choice: ")
    if ans == 'd':
        correct_ans = correct_ans + 1
    elif ans == 'a' or ans == 'b' or ans == 'c':
        wrong_ans += 1
    else:
        invalid_ans += 1


# question 3
def ques3():
    global correct_ans
    global wrong_ans
    global invalid_ans
    print("\n3. Which of the following disorders is the fear of being alone ?")
    print("\ta. Agoraphobia  \tb. Aerophobia \n\tc. Acrophobia   \td. Arachnophobia")
    ans = input("   Enter your choice: ")
    if ans == 'a':
        correct_ans = correct_ans + 1
    elif ans == 'b' or ans == 'c' or ans == 'd':
        wrong_ans += 1
    else:
        invalid_ans += 1


# question 4
def ques4():
    global correct_ans
    global wrong_ans
    global invalid_ans
    print("\n4. Which of the following animals can run the fastest ?")
    print("\ta. Leopard  \tb. Tiger \n\tc. Cheetah  \td. Lion")
    ans = input("   Enter your choice: ")
    if ans == 'c':
        correct_ans = correct_ans + 1
    elif ans == 'a' or ans == 'b' or ans == 'd':
        wrong_ans += 1
    else:
        invalid_ans += 1


# question 5
def ques5():
    global correct_ans
    global wrong_ans
    global invalid_ans
    print("\n5. How many time zones are there in total in the world ?")
    print("\ta. 8  \tb. 24 \n\tc. 16  \td. 32")
    ans = input("   Enter your choice: ")
    if ans == 'b':
        correct_ans = correct_ans + 1
    elif ans == 'a' or ans == 'c' or ans == 'd':
        wrong_ans += 1
    else:
        invalid_ans += 1


# print the correct answers if the users wishes so
def correctAns():
    print("\n1. What is the full form of RAM ? - a. Random Access Memory")
    print("\n2. Which is the only country that has a triangular flag ? - d. Nepal")
    print("\n3. Which of the following disorders is the fear of being alone ? - a. Agoraphobia")
    print("\n4. Which of the following animals can run the fastest ? - c. Cheetah")
    print("\n5. How many time zones are there in total in the world ? - b. 24")


# total number of question present
total_ques = 5
ques1()
ques2()
ques3()
ques4()
ques5()
print("\n\n\t\t\tYour Result: ")
print("\t\tTotal questions: ", total_ques)
print("\t\tCorrect: ", correct_ans)
print("\t\tWrong: ", wrong_ans)
print("\t\tInvalid answer: ", invalid_ans)

# ask if the user want to see the correct answers to each questions
choice = input("\n\nDo you want to view the correct answers ?(y/n): ")
if ch != 'y':
    print("Thank you for playing the game. Hope to see you again!!!!!!!!")
    time.sleep(2)
    exit()
correctAns()
print("\n\n\n\t\t\tThank you for playing the quiz game !!!!!!")
print("\n\t\t\tHope you enjoyed the game !!!!!!")
input("Enter any key to exit: ")

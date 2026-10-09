"""
Addition Quiz

Step1:Generate to single digit integer for number1(e.g.,4) and number2 (e.g.,5)
Step2:Prompt the student to answer,"what is 4+5>"(user input)
Step3:check whether the student answer is correct
"""
import random

level = 1

print("--- Welcome to the Math Test ---")

while True:
    if level == 1:
        num_1 = random.randint(1, 9)
        num_2 = random.randint(1, 9)
        
        answer = int(input(f"What is {num_1} + {num_2}? "))
        
        if answer == num_1 + num_2:
            print("Correct! Moving to Level 2...\n")
            level = 2
        else:
            print("Incorrect - try again\n")

    elif level == 2:
        num_3 = random.randint(1, 9)
        num_4 = random.randint(1, 9)
        
        answer1 = int(input(f"What is {num_3} * {num_4}? "))
        
        if answer1 == num_3 * num_4:
            print("Correct! Moving to Level 3...\n")
            level = 3
        else:
            print("Incorrect - try again\n")

    elif level == 3:
        num_5 = random.randint(1, 9)
        num_6 = random.randint(1, 5)
        
        answer2 = float(input(f"What is {num_5} / {num_6}? "))
        
        if answer2 == num_5 / num_6:
            print("Correct! You Passed the test 🎉")
            break
        else:
            print("Incorrect - try again\n")

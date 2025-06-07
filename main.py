# Project: Misinformation Trivia
# Coder: Rory Lehtola
# Date: 06/02/25
# Class: STEM 103 Spring


# Welcome the user and prompt them for their name also store it as a variable
def welcome_user():
    user_name=input("Welcome to the Misinformation Trivia! What's your name? ")
    print(f"Greetings {user_name}! Let's play a game!") # Greet the user by their name
    return user_name

welcome_user() 

# Imports
import random
import csv

# Load questions from CSV
def load_questions(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
           
        if not data: # File not found display for CSV
            print("Error!!! File not found")
            return None
    
        header = data[0] # Accessing data from CSV
        questions = data[1:]
        
        if not questions:
            print("Error!!! No questions found") # Questions not found display
            return None

        random.shuffle(questions) # Implement random question shuffle
        return questions
    
    except FileNotFoundError:
        print(f"Error!!! Could not find file '{file_path}'") # File not found error display
        return None

# Prompt the user to answer a question
def ask_question(q):
    question = q[0]
    choices = q[1:5]
    answer = q[5]

# Ask a question
    print("\n" + question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}.{choice}")
    
    is_continued = True
    while is_continued:
        try:
            user_input=int(input("Your answer (1-4): ")) # Prompt for user input
            if 1<=user_input<=4:
                is_continued=False
            else:
                print("Please enter a number between 1 and 4! ") # Ask user to input a # between 1-4
        except ValueError:
                print("That's not a valid number! Please try 1, 2, 3, or 4. ") # Error message for incorrect input
            
if choices[user_input-1].strip().lower()==answer.strip().lower():
    print("You got that totally right!") # Display for correct answer
    return True

else:
    print(f"Sorry, but that's incorrect. The correct answer is: {answer}") # Display for incorrect answer
    return False




# Keep track of the score


# Press enter to contiue prompt


# Display users name with the final score
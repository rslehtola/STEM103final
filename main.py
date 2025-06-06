# Project: Misinformation Station Trivia
# Coder: Rory Lehtola
# Date: 06/02/25
# Class: STEM 103 Spring


# Welcome the user and prompt them for their name also store it as a variable
def welcome_user():
    user_name=input("Welcome to the Misinformation Station Trivia! What's your name? ")
    print(f"Greetings {user_name}! Let's get started!") # Greet the user by their name
    return user_name

welcome_user() 

import random
import csv

# Load questions from CSV
def load_questions(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
           
        if not data: # File not found display for CSV
            print("File not found")
            return None
    
        header = data[0] # Loading from CSV
        questions = data[1:]
        
        if not questions:
            print("No questions found") # Questions not found display
            return None

        random.shuffle(questions) # Implement random question shuffle
        return questions
    
    except FileNotFoundError:
        print(f"Error!!! Could not find file '{file_path}'") # File not found error display
        return None

# Prompt the user to answer a question


# Prompt the user to input a number between 1-4


# Input user answer


# Check user answer is 1-4


# Error display on bad answer and prompt please pick an answer between 1-4 


# If users answer was correct display


# If user answer was incorrect display correct answer


# Keep track of the score


# Press enter to contiue prompt


# Display users name with the final score
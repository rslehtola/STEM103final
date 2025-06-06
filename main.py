# Project: Misinformation Station Trivia
# Coder: Rory Lehtola
# Date: 06/02/25
# Class: STEM 103 Spring

import random
import csv


# Welcome the user and prompt them for their name also store it as a variable
def welcome_user():
    user_name=input("Welcome to the Misinformation Station Trivia! What's your name?")
    print(f"Greetings {user_name}! Let's get started!") # Greet the user by their name
    return user_name

# Load questions from CSV
def load_questions(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader=csv.reader(file)
            data=list(reader)
            header=data[0]
            questions=data[1:]
            random.shuffle(questions)
            return questions
    except FileNotFoundError:
        print(f"Error!!! Could not find file '{file_path}'")
        return None

# Impement random question shuffle


# File not found error display


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
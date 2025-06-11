# Project: Misinformation Trivia
# Coder: Rory Lehtola
# Date: 06/16/25
# Class: STEM 103 Spring

# Program:
# Within this program is a beautiful trivia game. The questions for this game are completely 
# based on stupid comments and statemnets made by Donald Trump from which are inaccurate or untrue. 
# However, these questions and answers are true. Once ran, this program will welcome the user to 
# the game and prompt them to input their name. Once they input their name and hit enter it will 
# greet them by name and ask them to play a game and load the first question of twenty-four with 
# a multiple choice answer. The user only needs to input a number between 1-4 and hit enter. If 
# the user has answered the question incorrectly, it will display such and tell them what the 
# correct answer was and prompt them to hit enter to continue to the next question. If the user 
# answers the question correctly it will display a congradulation and prompt them to hit enter 
# when they're ready to continue to the next question. If the user doesn't answer with a number 
# between 1-4 it'll dispaly that it's not a valid number and ask them to please enter a 1, 2, 3, 
# or 4. Once all twenty-four questions are answered it displays your final score and shows good 
# sportsmanship with a good game and displaying the users name. I've attempted to answer my 
# questions with every symbol, character, letter, number and it won't accept any answer other 
# than 1, 2, 3 or 4.

# Function 1: Welcome the user and prompt them for their name also stores it as a variable
def welcome_user():
    user_name = input("Welcome to Misinformation Trivia! What's your name? ") # Ask for the users name
    print(f"Greetings {user_name}! Let's play a game!") # Greet the user by their name
    return user_name # Return users name to be used later

# Imports
import random # To shuffle questions randomly
import csv # To read questions from the CSV file

# Function 2: Load questions from CSV
def load_questions(file_path):
    try:
        with open(file_path, mode='r') as file: # Open the file to read mode
            reader = csv.reader(file) # Create a CSV reader object
            data = list(reader) # Convert the CSV reader to a list
           
        if not data: # Check if the file is empty
            print("Error!!! File is empty") # Inform user of empty file
            return None # Return none so the game doesn't continue

        questions = data[1:] # Store all the rows except the header as question data
        
        if not questions: # If there as no actual questions
            print("Error!!! No questions found") # Questions not found display
            return None # Stop game from continuing

        random.shuffle(questions) # Random question shuffle
        return questions # Return the loaded and shuffled questions

    except FileNotFoundError: # Handle the case where the file is not found
        print(f"Error!!! Could not find file '{file_path}'") # File not found error display
        return None # Stop crashes

# Function 3: Prompt the user to answer a question
def ask_question(q):
    question = q[0] # The questions text
    choices = q[1:5] # The four choices
    answer = q[5] # The correct answer

# Ask a question
    print("\n" + question) # Print the question
    for i, choice in enumerate(choices, 1): # Enumerate answer coices 1-4
        print(f"{i}.{choice}") # Display the choice with numbers
    
    is_continued = True # Control variable for input loop
    while is_continued: # Loop until valid input is received
        try:
            user_input = int(input("Your answer: ")) # Prompt user for answer
            if 1 <= user_input <= 4: # Validate number range
                is_continued = False # Exit loop on valid input
            else:
                print("Please enter a number between 1 and 4! ") # Ask user to input a # between 1-4
        except ValueError: # Catch non-integer input
                print("That's not a valid number! Please try 1, 2, 3, or 4. ") # Error message for incorrect input
            
    if user_input == int(answer.strip()):
        print("You got that totally right!") # Display for correct answer
        return True # Return True for score tracking
    else:
        print(f"Sorry, but that's incorrect. The correct answer is: {answer}") # Display for incorrect answer
        return False # Return False for score tracking

# Function 4: Keeps track of score
def run_quiz(questions):
    score = 0 # Initalize score to 0
    for q in questions: # Loop through each question
        if ask_question(q): # Call ask_questions and check if the answer is correct
            score += 1 # Add 1 to score if answer correct
        input("When you're ready, hit enter to continue: ") # Hit enter to continue to next question display
    return score # Return final score at the end
        
# Function 5: Display final score to user
def print_final_score(score, total, user_name):
    print(f"Good game, {user_name}. Your final score: {score}/{total}") # Good game with users name and final score display

# Function 6: Runs the full trivia game
def main():
    input_file = 'trivia_questions.csv' # File name for questions
    user_name = welcome_user() # Call the function to welcome user and get name
    questions = load_questions(input_file) # Load questions from CSV

    if questions: # If questions were loaded correctly
        score = run_quiz(questions) # Run the quiz and get final score
        print_final_score(score, len(questions), user_name) # Print final score and name

# Run the main function only if the script is enabled
if __name__ == "__main__":
    main() # Call the main function to start the most awesome game ever
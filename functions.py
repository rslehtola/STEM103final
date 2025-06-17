# Imports
import random
import csv

# Function 1: Welcome the user and prompt them for their name also stores it as a variable
def welcome_user():
    user_name = input("Welcome to Misinformation Trivia! What's your name? ") # Ask for the users name
    print(f"Greetings {user_name}! Let's play a game!") # Greet the user by their name
    return user_name # Return users name to be used later

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
        return None # Stops crashes

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
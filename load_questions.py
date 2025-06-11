# Imports
import csv
import random

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
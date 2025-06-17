# Imports
from functions import welcome_user
from functions import load_questions
from functions import run_quiz
from functions import print_final_score

# Function 6: Runs the full trivia game
def main():
    input_file = 'trivia_questions.csv' # File name for questions
    user_name = welcome_user() # Call the function to welcome user and get name
    questions = load_questions(input_file) # Load questions from CSV

    if questions: # If questions were loaded correctly
        score = run_quiz(questions) # Run the quiz and get final score
        print_final_score(score, len(questions), user_name) # Print final score and name

if __name__ == "__main__": # Runs code
    main()
# Imports
from ask_question import ask_question

# Function 4: Keeps track of score
def run_quiz(questions):
    score = 0 # Initalize score to 0
    for q in questions: # Loop through each question
        if ask_question(q): # Call ask_questions and check if the answer is correct
            score += 1 # Add 1 to score if answer correct
        input("When you're ready, hit enter to continue: ") # Hit enter to continue to next question display
    return score # Return final score at the end
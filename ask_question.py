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
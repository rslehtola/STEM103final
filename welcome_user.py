# Function 1: Welcome the user and prompt them for their name also stores it as a variable
def welcome_user():
    user_name = input("Welcome to Misinformation Trivia! What's your name? ") # Ask for the users name
    print(f"Greetings {user_name}! Let's play a game!") # Greet the user by their name
    return user_name # Return users name to be used later
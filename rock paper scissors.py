import random

# Print welcome message
print("Welcome to the Rock-Paper-Scissors game!")

# Define the game options
options = ["rock", "paper", "scissors"]

# Ask for user input
user_choice = input("Enter your choice (rock/paper/scissors): ")

# Validate user input
while user_choice.lower() not in options:
    user_choice = input("Invalid choice! Please choose again (rock/paper/scissors): ")

# Print user's choice
print(f"You chose {user_choice}.")

# Generate computer's choice
computer_choice = random.choice(options)
print(f"The computer chose {computer_choice}.")

# Determine the winner
if user_choice.lower() == computer_choice:
    print("It's a tie!")
elif (user_choice.lower() == "rock" and computer_choice == "scissors") or (user_choice.lower() == "paper" and computer_choice == "rock") or (user_choice.lower() == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
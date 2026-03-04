"""
Stone Paper Scissors Game
A simple command-line game where you play against the computer
"""

import random

# Welcome message
print("=" * 50)
print("Welcome to STONE PAPER SCISSORS!")
print("=" * 50)
print()

# Get player name
name = input("Enter your name: ")
print(f"Hello {name}! Let's play!")
print()

# Initialize scores
ps = 0  # player score
cs = 0  # computer score
ti = 0  # ties

# Available choices
ch = ["stone", "paper", "scissors"]

# Get number of rounds
rd = int(input("How many rounds do you want to play? "))
print()

# Game loop
for i in range(1, rd + 1):
    print(f"--- ROUND {i} ---")
    
    # Player's turn
    print("Choose: stone, paper, or scissors")
    pc = input("Your choice: ").lower()
    
    # Input validation
    while pc not in ch:
        print("Invalid choice! Please choose stone, paper, or scissors")
        pc = input("Your choice: ").lower()
    
    # Computer's turn
    cc = random.choice(ch)
    print(f"Computer chose: {cc}")
    
    # Determine winner
    if pc == cc:
        print("It's a TIE!")
        ti += 1  
    elif pc == "stone" and cc == "scissors":
        print(f"{name} WINS! Stone beats Scissors!")
        ps += 1
    elif pc == "scissors" and cc == "paper":
        print(f"{name} WINS! Scissors beats Paper!")
        ps += 1
    elif pc == "paper" and cc == "stone":
        print(f"{name} WINS! Paper beats Stone!")
        ps += 1
    else:
        print("Computer WINS!")
        cs += 1
    
    # Display current scores
    print(f"Score: {name} = {ps}, Computer = {cs}, Ties = {ti}")
    print()

# Final result
print("=" * 50)
print("GAME OVER!")
print("=" * 50)
print(f"{name}'s Score: {ps}")
print(f"Computer's Score: {cs}")
print(f"Ties: {ti}")
print()

# Declare winner
if ps > cs:
    print(f"Congratulations {name}! YOU WIN THE GAME!")
elif cs > ps:
    print("Computer wins the game! Better luck next time!")
else:
    print("It's a TIE GAME!")

print()
print("Thanks for playing!")
print("=" * 50)

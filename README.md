Stone Paper Scissors Game:

A simple and fun command-line game where you compete against the computer in the classic Stone-Paper-Scissors game.
Description
This is a Python-based implementation of the classic hand game Stone-Paper-Scissors (also known as Rock-Paper-Scissors). Play multiple rounds against the computer and see who comes out on top!
This project demonstrates fundamental programming concepts including loops, conditionals, input validation, and basic game logic. It's perfect for beginners learning Python or as a portfolio project.


Game Rules:

Stone beats Scissors (Stone crushes Scissors)
Scissors beats Paper (Scissors cuts Paper)
Paper beats Stone (Paper covers Stone)


Features:

Interactive command-line interface
Customizable number of rounds
Score tracking (Player, Computer, Ties)
Input validation for user choices
Round-by-round results display
Final winner declaration
Personalized gameplay with player name
Simple and clean code structure
No external dependencies required


How to Play:

1- Enter your name when prompted
2- Choose how many rounds you want to play
3- For each round, type your choice:
    stone
    paper
    scissors
4- The computer will randomly choose its move
5- The winner of each round is determined
6- After all rounds, the final winner is declared


Variables Used:

name - Player's name
ps - Player's score
cs - Computer's score
ti - Number of ties
ch - List of valid choices
rd - Number of rounds to play
pc - Player's choice
cc - Computer's choice
i - Round counter

Main Components:

1-  Welcome & Setup - Get player name and number of rounds
2-  Game Loop - Execute specified number of rounds
3-  Input Validation - Ensure valid choices
4-  Winner Determination - Compare choices and update scores
5-  Results Display - Show final scores and winner

Project Structure:

stone_paper_scissors_game
│
├── game.py              # Main game file
├── README.md            # This file
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
└── .gitignore          # Git ignore file

Enjoy the game! May the best player win!

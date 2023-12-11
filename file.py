# File Header
# Lluvia B and Kimberly Q
# November 29 2023
# define file classmethod
class File:
    filename=""
    
# File Header
# Lluvia B and Kimberly Q
# November 29 2023
# define file classmethod
import random

class File:
    filename = ""


# Set up the game
player1_hits = 0
player2_hits = 0
rounds = 0

# Game loop
while (player1_hits < 3 and player2_hits < 3):
    rounds +=1

    print(f"round {rounds}:")


    # Player 1's turn
    print("Player 1's turn:")
    player1_guess = random.randint(1, 10)
    player2_position = random.randint(1, 10)
    if player1_guess == player2_position:
        "if player2_hits + 1"

    print("Player 1 hit Player 2!")


    print("Player 1 missed.")


    # Player 2's turn
    print("Player 2's turn:")
    player2_guess = random.randint(1, 10)
    player1_position = random.randint(1, 10)
    if player2_guess == player1_position:
        player1_hits += 1

    print("Player 2 hit Player 1!")


    print("Player 2 missed.")

    print('')

    # Declare the winner

    if player1_hits == 3:

        print("Player 1 wins!")

    else:

        print("Player 2 wins!")

    print(f"Total rounds played: {rounds}")

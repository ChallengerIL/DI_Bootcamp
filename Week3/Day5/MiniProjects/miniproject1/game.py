# Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia
#
# We will create a game for the user to play Rock-paper-scissors against the computer.
#
#   - The user will input his/her move (rock/paper/scissors),
# and the computer will select either rock, paper or scissors at random.
#   - We will then compare the user’s move with the computer’s move, and determine the results of the game:
#
#   - The user won
#
#   - The computer won (the user lost)
#   - A draw (tie)
# We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.
#
# The user will be able to play again and again. Once the user decides to exit the program, we will print a summary of the outcomes of all the games: how many times they won, lost or and tied the computer.
#
# Here’s some example output:
#
# Mini Project2
#
# Instructions
# 1. Create a new directory for the game. Inside it, create 2 files:
#   1. rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
#   2. game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.
#
#
# Steps
# Part I - Game.Py
# 1. game.py – this file/module should contain a class called Game. It should have 4 methods:
#   1. get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.
#
#   2. get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).
#
#   3. get_game_result(self, user_item, computer_item) – Determine the result of the game.
#       - Parameters:
#           - user_item – the user’s chosen item (rock/paper/scissors)
#           - computer_item – the computer’s chosen (random) item (rock/paper/scissors)
#           - Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
#
#   4. play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
#       1. Get the user’s item (rock/paper/scissors) and remember it
#
#       2. Get a random item for the computer (rock/paper/scissors) and remember it
#
#       3. Determine the results of the game by comparing the user’s item and the computer’s item
#           1. Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
#
#           2. Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
#
#
# Part II - Rock-Paper-Scissors.Py
# 1. rock-paper-scissors.py : create 3 functions
#   1. get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit
#
#   2. print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.
#
#
# Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.
#
#   3. main() - the main function. It should take care of 3 things:
#       1. Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)
#
#       2. When the user chooses to play a game:
#           - Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
#           - Remember the results of every game that is played.
#
#       3. When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.

from random import choice


class Game:

    OPTIONS = ["rock", "paper", "scissors"]

    def __init__(self):
        self.user_item = None
        self.computer_item = None
        self.score = {
            "win": 0,
            "loss": 0,
            "draw": 0,
        }

    def get_user_item(self):
        user_item = None
        print("Your options are:")
        [print(f"{i} - {item}") for i, item in enumerate(self.OPTIONS)]

        while not user_item:
            try:
                user_input = int(input("Enter your choice as a number: ").strip()[0])
                if user_input < 0 or user_input > len(self.OPTIONS)-1:
                    print("Invalid choice, the number must be between 0 and 2")
                    continue
            except ValueError:
                print("Wrong input, only numbers are allowed")
            else:
                user_item = self.OPTIONS[user_input]

                return user_item

    def get_computer_item(self):
        computer_item = choice(self.OPTIONS)

        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            self.score["draw"] += 1
            return "draw"
        elif user_item == "rock" and computer_item == "scissors":
            self.score["win"] += 1
            return "win"
        elif user_item == "paper" and computer_item == "rock":
            self.score["win"] += 1
            return "win"
        elif user_item == "scissors" and computer_item == "paper":
            self.score["win"] += 1
            return "win"
        else:
            self.score["loss"] += 1
            return "loss"

    def play(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()

        result = self.get_game_result(self.user_item, self.computer_item)
        print(f"You selected {self.user_item}. The computer selected {self.computer_item}. The result is a {result}")

        return result

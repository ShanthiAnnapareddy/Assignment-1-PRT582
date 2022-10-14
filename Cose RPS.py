import random
import math
import sys


class GameMain:
    TOTAL_WIN_COUNT = 5
    OPTIONS = ["rock", "paper", "scissors"]

    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def takeInputFromPlayerAndComputer(self):

        while True:
            userInput = input(
                "Choose anyone between these three: rock, paper or scissors. Press (q) to quit the game or Press (r) for restart the game \n"
            )
            userInput = userInput.lower()
            # restart option
            if userInput == "r":
                self.main()
            # quit game
            if userInput == "q":
                sys.exit()

            if userInput not in self.OPTIONS:
                print("you selected the wrong option")
                continue
            else:
                break

        computer_input = self.computerInput()

        if userInput == computer_input:
            return (0, userInput, computer_input)

        # rock > scissors, scissors > paper, paper > rock
        if self.isWin(userInput, computer_input):
            return (1, userInput, computer_input)

        return (-1, userInput, computer_input)

    def computerInput(self):
        return random.choice(self.OPTIONS)

    def isWin(self, player, computer):
        # return true is the player beats the computer
        # winning conditions: r > s, s > p, p > r
        if (
            (player == "rock" and computer == "scissors")
            or (player == "scissors" and computer == "paper")
            or (player == "p" and computer == "r")
        ):
            return True
        return False

    def play(self):
        # play against the computer until someone wins best of n games

        self.player_wins = 0
        self.computer_wins = 0

        while self.player_wins < self.TOTAL_WIN_COUNT and self.computer_wins < self.TOTAL_WIN_COUNT:
            result, user, computer = self.takeInputFromPlayerAndComputer()
            # tie
            if result == 0:
                print(
                    "It is a tie. \n".format(
                        user
                    )
                )
            # you win
            elif result == 1:
                self.player_wins += 1
                print(
                    "You chose {} and the computer chose {}. You won {} times \n".format(
                        user, computer, self.player_wins
                    )
                )
            else:
                self.computer_wins += 1
                print(
                    "You chose {} and the computer chose {}. You lost sorry.. The computer won {}\n".format(
                        user, computer, self.computer_wins
                    )
                )

        if self.player_wins > self.computer_wins:
            print(
                "Player  won the game "
            )
        else:
            print(
                " The computer has won the game!!"
            )

    def main(self):
        print("Restart the game")
        self.play()

    def doAnyWinTheGame(self):
        # return true is the player beats the computer
        # winning conditions: r > s, s > p, p > r
        if self.player_wins >= 5 or self.computer_wins >= 5:
            return True
        return False


if __name__ == "__main__":
    game = GameMain()
    game.play()

import unittest

from GameMain import GameMain


# @patch('builtins.print')
class UnitTestMainGame(unittest.TestCase):

    def test_player_wins_computer_with_rock_smashes_paper(self):
        game = GameMain()
        user_action = "rock"
        computer_action = "scissors"
        assert (game.isWin(user_action, computer_action) == True)

    def test_GameWinsWithFivePoints(self):
        game = GameMain()
        game.player_wins = 4
        game.computer_wins = 0
        assert game.doAnyWinTheGame() != True

        game.playerWins = 5
        assert game.doAnyWinTheGame() == True


if __name__ == "__main__":
    unittest.main()

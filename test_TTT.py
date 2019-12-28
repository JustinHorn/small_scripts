import unittest
import TicTacToe

class Test_TTT(unittest.TestCase):

    def test_setWin(self): # YOU REALLY NEED TO MAKE YOUR BREAKS :D
        TicTacToe.set_win('O') # Wieso werden die Werte nicht überschrieben?
        self.assertEqual(False,TicTacToe.game_running)
        self.assertEqual('O',TicTacToe.WINNER)
    
 

        

if __name__ == '__main__': # if you call only python test_TTT.py - it will call unittest.main()
    unittest.main()
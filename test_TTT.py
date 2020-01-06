import unittest
from TicTacToe import TTT
import random

class Test_TTT(unittest.TestCase):

    def test_standards(self):
        ttt = TTT()
        self.assertEqual(' ',ttt.EMPTY)
        self.assertEqual(9,len(ttt.field))

    def test_make_move(self): 
        ttt = TTT()
        for i in range(9):
            ttt.make_move(0)
            self.assertEqual(ttt.field[0],ttt.PLAYER_SIGNS[ttt.current_player])
            ttt.swap_player()

    def test_is_gameOver_whoWon(self):
        ttt = TTT()
        for i in range(7):
            ttt.make_move(i)
            ttt.swap_player()
            if i < 6:
                self.assertEqual(ttt.is_gameOver_whoWon()[0],False)
            else:
                self.assertEqual(ttt.is_gameOver_whoWon()[0],True)

    
    def test_readModelFromFile(self):
        ttt = TTT()
        ttt.readModelFromFile()

    def test_play_random_vs_random(self):
        ttt,get_randomMove = funcAndTTT()

        for i in range(9):    
            ttt.reset
            ttt._play([get_randomMove,get_randomMove],show=False)

    def test_play_ai_vs_random(self):
        ttt,get_randomMove = funcAndTTT()

        for i in range(9):    
            ttt.reset
            ttt._play([ttt.get_NNMove,get_randomMove],show=False)

    def test_play_ai_vs_ai(self):
        ttt = TTT()

        for i in range(9):    
            ttt.reset
            ttt._play([ttt.get_NNMove,ttt.get_NNMove],show=False)



def funcAndTTT():
    ttt = TTT()
    def get_randomMove():
        m = []
        for i in range(9):
            if ttt.is_moveLegal(i):
                m.append(i)
        i = random.randrange(0,len(m))
        return m[i]
    return ttt, get_randomMove   

if __name__ == '__main__': # if you call only python test_TTT.py - it will call unittest.main()
    unittest.main()
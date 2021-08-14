
import numpy as np
import pickle
import random
from model import *

class TTT():

    def __init__(self):
        self.EMPTY = ' '
        self.PLAYER_SIGNS = ['X','O']
        self.reset()
        self.readModelFromFile()

    def reset(self):
        self.EMPTY = ' '
        self.current_player = 0
        self.field = [' ']*9
        self.game_over = False


    def play_hVsH(self): #to Test
        move_func = [self.get_humanMove]*2
        self._match(move_func)

    def play_humanVsMachine(self,humanstarts:bool=True): # to test
        move_func = [self.get_humanMove,self.get_NNMove]
        if not humanstarts:
            move_func = move_func.reverse()
        self._match(move_func)    

    def readModelFromFile(self):
        with open('TTT_NN_FILES\TTTnn.pkl', 'rb') as input_stream:
            self.model = pickle.load(input_stream)
        pass

    def _match(self, get_move:list,show=False,startRandom=False):# to Test
        self.reset()
        if startRandom:
            self.field[random.randrange(0,9)] = [self.PLAYER_SIGNS[0]]
            self.current_player = 1
        while not self.game_over:
            if show:
                self.display_field()
            m = get_move[self.current_player](self.field)
            if self.is_moveLegal(m):
                self.make_move(m)
                (self.game_over ,WINNER) = self.eval_game()
                if not self.game_over:
                    self.nextPlayer()
            else:
                print("Illegal move!")
        if show:
            self.display_field()
            self.send_endMessage(WINNER)
        return WINNER

    def get_NNMove(self,field): # to Test
        inputVector = TTT.fieldToList(field,self.EMPTY,self.PLAYER_SIGNS)
        moveTensor = self.model.predict([inputVector])
        moveVector =(moveTensor).numpy().astype(np.float32)[0]
        m =  TTT.vectorToMove(moveVector)
        while not self.is_moveLegal(m):
            moveVector[m] = -99999999.0
            m =  TTT.vectorToMove( moveVector)
        return m

     
    def get_humanMove(self,field):
        string = "Enter the field you want to mark Player " + self.PLAYER_SIGNS[self.current_player] + ": (0-8):"
        while True:
            try:
                move = int(input(string))
            except ValueError:
                print("You need to write an Integer")
                continue
            else:
                return move

    def is_moveLegal(self,move):
        return  self.field[move] == self.EMPTY;

    @staticmethod
    def moveLegal(field,move,EMPTY=' '):
        return  field[move] == EMPTY;

    def make_move(self,move): # i guess it associates type at init
        self.field[move] = self.PLAYER_SIGNS[self.current_player]

    def eval_game(self): #to Test
        field = self.field
        for i in range(0,3):
            if (same(field,[x+i*3 for x in [0,1,2]]) and  field[i*3] != self.EMPTY):  #horizontal
                return True, field[i*3]
            if (same(field,[x+i for x in [0,3,6]])  and  field[i] != self.EMPTY):#vertical
                return True,field[i]
        if ( same(field,[0,4,8]) and  field[4] != self.EMPTY): # diagonal1
            return True,field[4]
        if ( same(field,[2,4,6]) and  field[4] != self.EMPTY): #diagonal2
            return True,field[4]
        for pos in field:  # not over
            if pos == self.EMPTY:
                return False,self.EMPTY
        return True,self.EMPTY

    def nextPlayer(self):
        self.current_player = 1 if self.current_player == 0 else 0;

    def send_endMessage(self,WINNER):
        print("Congretulations Player ",WINNER," you won!");
    
    def display_field(self):
        field = self.field
        for i in range(3):
            if not i== 0: print("---------")
            print(field[i*3],"|",field[1+i*3],"|",field[2+i*3])
    
    @staticmethod
    def fieldToList(field,EMPTY=' ',PLAYER_SIGNS=['X','O']):
        vector = []
        for char in field:
            x = [0.01]*3
            if char ==EMPTY:
                x[0] = 0.99
            elif char ==PLAYER_SIGNS[1]:
                x[1] = 0.99
            else:
                x[2] = 0.99
            for e in x:
                vector.append(e)
        return vector

    @staticmethod
    def  fieldToVector(field,EMPTY,PLAYER_SIGNS):
        l = TTT.fieldToList(field,EMPTY,PLAYER_SIGNS)
        return np.array(l).astype(np.float32)
    
    @staticmethod
    def  fieldToVector(field):
        l = TTT.fieldToList(field)
        return np.array(l).astype(np.float32)

    @staticmethod
    def vectorToMove(vector):
        return np.argmax(vector)
        



def same(arr, list_of_indexes):
    for index in list_of_indexes:
        if arr[list_of_indexes[0]] != arr[index]:return False
    return True;
################### MAIN ##############################

# game = TTT()
# # print(game.fieldToInputVector().shape)
# # print(game.fieldToInputVector())
# game.readModelFromFile()
# print("Ai vs Ai,", game.AImatch([game.model.predict,game.model.predict]))
# #game.display_field()


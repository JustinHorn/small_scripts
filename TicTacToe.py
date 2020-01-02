
import numpy as np
import pickle


class TTT():

    def __init__(self):
        self.EMPTY = ' '
        self.PLAYER_SIGNS = ['X','O']
        self.current_player = 0
        self.field = [' ']*9
        self.model = None

    def play_hVsH(self):
        move_func = [self.get_humanMove]*2
        self._play(move_func)

    def play_humanVsMachine(self,humanstarts:bool=True):
        if self.model == None:
            with open('TTTnn.pkl', 'rb') as input_stream:
                self.model = pickle.load(input_stream)

        move_func = [self.get_humanMove,self.get_NNMove]
        if not humanstarts:
            move_func = move_func.reverse()
        self._play(move_func)    

    def _play(self, get_move):
        self.field = [' ']*9
        game_over = False
        while not game_over:
            self.display_field()
            m = get_move[self.current_player]()
            if self.is_moveLegal(m):
                self.make_move(m)
                (game_over ,WINNER) = self.is_gameOver_whoWon()
                if not game_over:
                    self.swap_player()
        self.display_field()
        self.send_endMessage(WINNER)

    def get_NNMove(self):
        field_as_inputVector = self.fieldToInputVector()
        move_as_vector = self.model.predict([field_as_inputVector])
        return self.outputVectorToMove( move_as_vector)
          
     
    def get_humanMove(self):
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
        field = self.field
        return  self.field[move] == self.EMPTY;

    def make_move(self,move): # i guess it associates type at init
        self.field[move] = self.PLAYER_SIGNS[self.current_player]

    def is_gameOver_whoWon(self):
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

    def swap_player(self):
        self.current_player = 1 if self.current_player == 0 else 0;

    def send_endMessage(self,WINNER):
        print("Congretulations Player ",WINNER," you won!");
    
    def display_field(self):
        field = self.field
        for i in range(3):
            if not i== 0: print("---------")
            print(field[i*3],"|",field[1+i*3],"|",field[2+i*3])
    
    def fieldToInputVector(self):
        field = self.field
        vector = []
        for char in field:
            x = [0.01]*3
            if char == self.EMPTY:
                x[0] = 0.99
            elif char == self.PLAYER_SIGNS[1]:
                x[1] = 0.99
            else:
                x[2] = 0.99
            for e in x:
                vector.append(e)
        return np.array(vector).astype(np.float32)
    
    def outputVectorToMove(self,vector):
        return np.argmax(vector)



def same(arr, list_of_indexes):
    for index in list_of_indexes:
        if arr[list_of_indexes[0]] != arr[index]:return False
    return True;
################### MAIN ##############################

game = TTT()
# print(game.fieldToInputVector().shape)
# print(game.fieldToInputVector())

game.play_humanVsMachine()
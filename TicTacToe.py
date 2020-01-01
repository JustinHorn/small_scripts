
class TTT():

    def __init__(self):
        self.EMPTY = ' '
        self.PLAYER_SIGNS = ['X','O']
        self.current_player = 0
        self.field = [' ']*9

    def play_hVsH(self):
        move_func = [self.get_humanMove]*2
        self._play(move_func)

    def play_humanVsMachine(self,humanFirst:bool):
        move_func = [self.get_humanMove,self.get_NNMove]
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

    def get_nnMove(self,field=None):
        if field == None: field = self.field
        return model.predict(field)
          
     
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

    def is_moveLegal(self,move,field=None):
        if field == None: field = self.field
        return  self.field[move] == self.EMPTY;

    def make_move(self,move): # i guess it associates type at init
        self.field[move] = self.PLAYER_SIGNS[self.current_player]

    def is_gameOver_whoWon(self,field=None):
        if field == None: field = self.field
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
    
    def display_field(self,field=None):
        if field == None: field = self.field
        for i in range(3):
            if not i== 0: print("---------")
            print(field[i*3],"|",field[1+i*3],"|",field[2+i*3])
    



def same(arr, list):
    for i in list:
        if i and arr[list[0]] != arr[i]:return False
    return True;
################### MAIN ##############################

game = TTT()
game.play_hVsH()
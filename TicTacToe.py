
class TTT():
    game_over = False;
    X = 'X'
    O = 'O'
    EMPTY = ' '
    PLAYER_SIGNS = [X,O]
    current_player = 0
    SIZE = 9
    WINNER = None
    field = [' ']*9

    def play(self):
        while not self.game_over:
            self.display_field()
            m = self.ask_for_move()
            if self.is_moveLegal(m):
                self.make_move(m)
                (self.game_over ,self.WINNER) = self.is_gameOver_whoWon()
                if not self.game_over:
                    self.swap_player()
        self.display_field()
        self.send_end_message()


    def ask_for_move(self):
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

    def make_move(self,move): # i guess it associates type at init
        self.field[move] = self.PLAYER_SIGNS[self.current_player]

    def is_gameOver_whoWon(self):
        field = self.field
        for i in range(0,3):
            if ((field[i*3] ==field[1+i*3] ) and (field[1+i*3] == field[2+i*3]) and  field[i*3] != self.EMPTY):  #horizontal
                return True, field[i*3]
            if (( field[i] ==field[i+1*3]) and ( field[i+1*3] == field[i+2*3]) and  field[i] != self.EMPTY):#vertical
                return True,field[i]
        if ( (field[0] ==field[4]) and (field[4] == field[8]) and  field[4] != self.EMPTY): # diagonal1
            return True,field[4]
        if ( (field[2] ==field[4] )and (field[4] == field[6]) and  field[4] != self.EMPTY): #diagonal2
            return True,field[4]
        for pos in field:  # not over
            if pos == self.EMPTY:
                return False,self.EMPTY
        return True,self.EMPTY

    def swap_player(self):
        self.current_player = 1 if self.current_player == 0 else 0;

    def send_end_message(self):
        print("Congretulations Player ",self.WINNER," you won!");
    
    def display_field(self):
        field = self.field
        for i in range(3):
            if not i== 0: print("---------")
            print(field[i*3],"|",field[1+i*3],"|",field[2+i*3])

################### MAIN ##############################
game = TTT();
game.game_over =True
game2 = TTT()
game2.play()
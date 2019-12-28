

def play():
    game_over = False;
    X = 'X'
    O = 'O'
    EMPTY = ' '
    PLAYER_SIGNS = [X,O]
    current_player = 0
    SIZE = 9
    WINNER = None
   
    field = get_startField()
    while not game_over:
        display_field()
        m = ask_for_move()
        if test_moveLegal(m):
            make_move(m,signs= PLAYER_SIGNS ,curr_pl=current_player)
            (game_over ,WINNER) = is_gameOver_whoWon(field)
            if not game_over:
                current_player = swap_players(current_player)
    display_field(field)
    send_end_message(WINNER)

#tehre are sets/Mengen in Python

def  get_startField(SIZE):
    return [' ']*SIZE

def display_field(field):
    for i in range(3):
        if not i== 0: print("---------")
        print(field[i*3],"|",field[1+i*3],"|",field[2+i*3])


def ask_for_move():
    string = "Enter the field you want to mark Player " + PLAYER_SIGNS[current_player] + ": (0-8):"
    while True:
        try:
            move = int(input(string))
        except ValueError:
            print("You need to write an Integer")
            continue
        else:
            return move


def test_moveLegal(move):
    return  field[move] == EMPTY;

def make_move(move:int, curr_pl = 0): # i guess it associates type at init
    field[move] = signs[curr_pl]

def set_win(field:str):
    global game_running 
    game_running= False
    global WINNER
    WINNER = field

def is_gameOver_whoWon(field):
    for i in range(0,3):
        if ((field[i*3] ==field[1+i*3] ) and (field[1+i*3] == field[2+i*3]) and  field[i*3] != EMPTY):  #horizontal
            return True, field[i*3]
        if (( field[i] ==field[i+1*3]) and ( field[i+1*3] == field[i+2*3]) and  field[i] != EMPTY):#vertical
            return True,field[i]
    if ( (field[0] ==field[4]) and (field[4] == field[8]) and  field[4] != EMPTY): # diagonal1
            return True,field[4]
    if ( (field[2] ==field[4] )and (field[4] == field[6]) and  field[4] != EMPTY): #diagonal2
            return True,field[4]
    for pos in field:  # not over
        if pos == EMPTY:
            return False,EMPTY
    return True,EMPTY

def swap_players(current_player):
    return 1 if current_player == 0 else 0;

def send_end_message(WINNER):
    print("Congretulations Player ", WINNER," you won!");
################### MAIN ##############################

play()
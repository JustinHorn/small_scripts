#include <stdio.h>

#define FALSE 0
#define TRUE 1
#define FIELD_SIZE	9
#define PLAYER_COUNT	2
#define PLAYER_ONE	0
#define PLAYER_TWO	1
#define EMPTY_FIELD 	-1
#define GAME_RUNNING	EMPTY_FIELD
#define TIE		-2
#define VICTORY_PLAYER_ONE PLAYER_ONE
#define VICTORY_PLAYER_TWO PLAYER_TWO


void generateField(int field[]);
void setChar_of_Player(int player);
int game_status(int field[]);
int int_elements_equal(int x, int y , int z);
void update_char_field(int field[]);
void showField(char field[]);
int getMove(int currentPlayer);
int is_move_legal(int field[], int move);
void doMove(int move,int  currentPLayer); // I doubt that this funciton was necessary
int getNextPLayer();
void announceEnd();

int field[FIELD_SIZE];
char char_field[FIELD_SIZE];
char playerChars[2];
int currentPlayer = PLAYER_ONE;


int main() {
	generateField();
	setChar_of_Player(PLAYER_ONE);
	setChar_of_Player(PLAYER_TWO);
	while(game_status() == GAME_RUNNING) {
		showField();
		int move = getMove(currentPLayer);
		if(is_move_legal(field,move) == TRUE) {
			doMove(move, currentPLayer);
		}
		if(game_status() == GAME_RUNNING) {
			currentPlayer = getNextPLayer();
			showField();
			int move = getMove(currentPLayer);
			if(is_move_legal(field,move) == TRUE) {
				doMove(move, currentPLayer);
			}
		}
		currentPlayer = getNextPLayer();
	}
	announceEnd();
}



void generateField(int field[]); {
	for(int i = 0; i < FIELD_SIZE;i++) {
		field[i] = -1;
	}
}

void setChar_of_Player(int player) {
	printf("Enter char of Player %d: \n",player);
	playerChars[player] = getChar();
}


int game_status(int field[]) {
	for(int i = 0; i < 3;i++) { // horizontal
		if(field[i] != -1 && int_elements_equal(field[i],field[i+1],field[i+2]) == TRUE) {
			return field[i];
		}
	}

	for(int i = 0; i < 3;i++) { // vertical
		if(field[i] != -1 && int_elements_equal(field[i],field[i+3],field[i+6]) == TRUE) {
			return field[i];
		}
	}


	if(field[4] != -1 && int_elements_equal(field[0],field[4],field[8]) == TRUE) {
		return field[4];
	}
	if(field[4] != -1 && int_elements_equal(field[2],field[4],field[6]) == TRUE) {
		return field[4];
	}
	return GAME_RUNNING;
}

int int_elements_equal(int x, int y , int z) {
	if(x == y && x == z) {
		return TRUE;
	}
	return FALSE;
}

void showField(char field[]) {
	update_char_field(field);
	printf("%d | %d | %d\n",char_field[0],char_field[1],char_field[2]);
	printf(" - + - + -\n");
	printf("%d | %d | %d\n",char_field[0],char_field[1],char_field[2]);
	printf(" - + - + -\n");
	printf("%d | %d | %d\n",char_field[0],char_field[1],char_field[2]);
}

void update_char_field(int field[]) {
	for(int i = 0; i < FIELD_SIZE;i++) {
		char x;
		if(field[i] == EMPTY_FIELD) {
			x = ' ';
		} else{
			x = playerChars[field[i]];
		}
		char_field[i] = x;
	}
}

int getMove(int current_Player) {
	printf("Its your turn Player %d or %c ! Make a move(0-8): \n",currentPlayer, playerChars[currentPlayer]);

	return getChar();
}

int is_move_legal(int field[], int move) {
	if(field[move] == EMPTY_FIELD) {
		return TRUE;
	} else {
		return FALSE;
	}
}

void doMove(int move, int currentPLayer) {
	field[move] = currentPlayer; 
}

int getNextPLayer() {
	if(currentPlayer == PLAYDER_ONE) {
		return PLAYER_TWO;
	} else {
		return PLAYER_ONE;
	}
}

void announceEnd() {
	int x = game_status();
	if(x == TIE) {
		printf("It is a tie!");
	} else {
		printf("Congretulations Player %d // %c you won!",x,playerChars[x]);
	}
}

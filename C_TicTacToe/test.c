#include <stdio.h>

#define CURRENTWORLD_INDEX 0
void 	useAnArray();

int birthday = 19022000;
int birthday2 = 19022000;

int main() {
	
	//extern ... needed when variable is declared in another file

	printf("Hello world \t %d \n",CURRENTWORLD_INDEX);
	printf("Hello Justin \t %d \n",birthday);// 1902...
	int birthday;
	printf("Hello Justin \t %d \n",birthday); // 0
	//string a = scanf("In which world are we?");
	//printf("%s",a);
	useAnArray();
	char a  = '\n';
}

void	useAnArray() {
	int array[10];
	array[1] =getchar();
	for(int i = 0; i < array[1];i++) {

		printf("\t %d \t \n",i);
	}
	printf("\t %c \t \n",(char)array[1]); // displays the int as a character
}


void	loop() {
	int c;

	while((c = getchar()) != 'P') { // != > =
		putchar(c);

	}
}

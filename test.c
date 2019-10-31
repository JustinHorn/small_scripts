#include <stdio.h>

#define CURRENTWORLD_INDEX 0

int main() {

	printf("Hello world \t %d \n",CURRENTWORLD_INDEX);
	//string a = scanf("In which world are we?");
	//printf("%s",a);
	int c;

	while((c = getchar()) != 'P') {
		putchar(c);

	}
}

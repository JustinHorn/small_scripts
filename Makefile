# Please write your make-skript here
SOURCE = TTT
all: TTT

TTT: 
	clang -o $(SOURCE) -std=c11 -pedantic -Wall -Wextra $(SOURCE).c
doTTT: TTT
	./test

test: 
	clang -o $(SOURCE) -std=c11 -pedantic -Wall -Wextra $(SOURCE).c
doTest: test
	./test
%.o:%.c
	gcc -c $<
.PHONY: all test  TTT clean
clean:
	rm -f *.o test

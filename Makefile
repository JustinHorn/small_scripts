# Please write your make-skript here
SOURCE = test
all: test doTest

test: 
	clang -o $(SOURCE) -std=c11 -pedantic -Wall -Wextra $(SOURCE).c
doTest: test
	./test
%.o:%.c
	gcc -c $<
.PHONY: all test clean
clean:
	rm -f *.o test

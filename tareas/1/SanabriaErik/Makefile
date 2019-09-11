#https://opensource.com/article/18/8/what-how-makefile

CC = gcc
SOURCE = hello.c

all:
	${CC} ${SOURCE} -o exec -lpthread
	
debug:
	${CC} ${SOURCE} -g -o exec -lpthread
    
clean:
	rm -v exec


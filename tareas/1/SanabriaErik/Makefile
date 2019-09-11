#https://opensource.com/article/18/8/what-how-makefile

CC = gcc
SOURCE = source.c

all:
	${CC} ${SOURCE} -m64 -o exec -lpthread
	
debug:
	${CC} ${SOURCE} -g -m64 -o exec -lpthread
    
clean:
	rm -v exec


ass:
	${CC} -S -masm=intel ${SOURCE}

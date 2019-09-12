#https://opensource.com/article/18/8/what-how-makefile

CC = gcc
SOURCE = source.c

release:
	${CC} ${SOURCE} -m64 -o exec -lpthread
	
all:
	${CC} ${SOURCE} -g2 -O0 -m64 -o exec -lpthread
    
clean:
	rm -v exec core*


ass:
	${CC} -S -masm=intel ${SOURCE}

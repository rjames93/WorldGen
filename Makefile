CC=g++ -std=gnu++11 
CFLAGS=-g3 -pedantic -Wall -Wextra 
INCLUDES=-I/usr/local/include -I.
LDFLAGS=-lm -lGL -lglfw
BinaryName=WorldGen.app


OBJS=main.o IcoSphere.o utilityfunctions.o
all: $(OBJS) $(BinaryName)
%.o:	%.cpp
	$(CC) $(CFLAGS) $(INCLUDES) -c $<

$(BinaryName):
	$(CC) -o $(BinaryName) $(LDFLAGS) $(INCLUDES) $(OBJS)

clean:
	rm -rf *.o $(BinaryName)

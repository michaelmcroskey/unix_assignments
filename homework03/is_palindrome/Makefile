CC=		gcc
CFLAGS=		-Wall -g -gdwarf-2 -std=c99 -std=gnu99
TARGETS=	is_palindrome

all:	$(TARGETS)

%.o:	%.c
	$(CC) -c $(CFLAGS) -o $@ $^
	valgrind --leak-check=full $^

clean:
	rm -f $(TARGETS) *.o
all:	hello-dynamic.o hello-static.o hello-debug.o hello-profile.o

hello-dynamic.o: hello.c
	gcc -o hello-dynamic hello.c

hello-static.o: hello.c
	gcc -o hello-static hello.c -static

hello-debug.o: hello.c
	gcc -o hello-debug hello.c -g

hello-profile.o: hello.c
	gcc -o hello-profile hello.c -pg

clean:
	rm *.o hello
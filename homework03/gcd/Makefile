CC=		gcc
CFLAGS=		-Wall -g -gdwarf-2
LD=		gcc
LDFLAGS=	-shared
AR=		ar
ARFLAGS=	crs
TARGETS=	libgcd.a libgcd.so gcd-static gcd-dynamic

all:	$(TARGETS)

# static executable
gcd-static: main.o libgcd.a
	$(LD) -static -o gcd-static main.o libgcd.a

# dynamic executable
gcd-dynamic: main.o libgcd.so
	$(LD) -o gcd-dynamic libgcd.so main.o
	

libgcd.a: gcd.o
	$(AR) $(ARFLAGS) libgcd.a gcd.o

	
libgcd.so: gcd.o
	$(LD) $(LDFLAGS) -o libgcd.so gcd.o
	

%.o:	%.c
	$(CC) -c $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS) *.o
example: $(_ID_).o
	       gcc -o /dev/stdout $(_ID_).o

$(_ID_).o: main.c
	       gcc -o $(_ID_).o -c main.c -W -Wall -D _FLAG_="\"$(_FLAG_)\""

clean:
	rm *.o

#!/usr/bin/env python3
#def lucas():
#	a = 2
#	b = 1
#	while True:
#		yield b
#
#for x in lucas():
#	print(x)

million_squares = (x*x for x in range(1,10001))
print(list(million_squares))

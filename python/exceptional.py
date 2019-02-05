#!/usr/bin/enb python3
'''A module for demonstrating exceptions.'''

def convert(s):
	'''Convert to an integer.'''
	try:
		x = int(s)
	except ValueError:
		x = -1
	return x

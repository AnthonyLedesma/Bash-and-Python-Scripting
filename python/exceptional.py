#!/usr/bin/enb python3
'''A module for demonstrating exceptions.'''

def convert(s):
	'''Convert to an integer.'''
	try:
		x = int(s)
		print("Conversion succeeded!")
	except (ValueError, TypeError):
		x = -1
		print("Conversion failed")
	return x

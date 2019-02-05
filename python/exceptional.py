#!/usr/bin/enb python3
'''A module for demonstrating exceptions.'''
import sys
#def convert(s):
#	'''Convert to an integer.'''
#	try:
#		x = int(s)
#		print("Conversion succeeded!")
#	except (ValueError, TypeError):
#		x = -1
#		print("Conversion failed")
#	return x

def convert(s):
	'''Convert to an integer.'''
	try:
		return int(s)
	except (ValueError, TypeError) as err:
		print("Conversion error: {}"\
			.format(str(err)),
			file=sys.stderr)
	return -1
#!/usr/bin/python3
"""
simple functio to print the content of file
"""


def read_file(filename=""):
	"""using with statement"""
	with open(filename, 'r', encoding =  'UTF8') as M:
		print(M.read())

"""
Main Script
"""

import argparse
from readfile import *
from readexpression import *

parser = argparse.ArgumentParser(description='Evaluate the arithmetic expressions.')
parser.add_argument('-i', '--inputfile', type=str, help='Input file')
parser.add_argument('-dPN', '--digitsPerNode', type=int, help='Number of digits to divide by')
args = parser.parse_args()

def main():
	
	input_file = "pycode.txt"
	num_of_digits = 2

	expressions = []
	results = []

	read_file(input_file, expressions)

	for exp in expressions:
		read_expression(exp, num_of_digits, results)

	for n in range(len(expressions)):
		print(expressions[n], '=', results[n])

if __name__ == "__main__":
	main()
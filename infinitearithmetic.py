"""
Main Script
"""

import argparse
from readfile import *

parser = argparse.ArgumentParser(description='Evaluate the arithmetic expressions.')
parser.add_argument('-i', '--input', type=str, help='Input file')
parser.add_argument('-dPN', '--digitsPerNode', type=int, help='Number of digits to divide by')
args = parser.parse_args()

def main():
	
	input_file = "pycode.txt"
	num_of_digits = 2

	read_file(input_file)

if __name__ == "__main__":
	main()
""" 
Reading File Script
"""

import re

def read_file(input_file):

	pattern = re.compile('(multiply|add)\(\d*,\d*\)')

	with open(input_file) as file:
		lines = file.read()

		matches = pattern.finditer(lines)

		for match in matches:
			print(match)

	file.close()


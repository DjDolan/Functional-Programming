""" 
Reading File Script
"""

import re

def read_file(input_file):

	pattern = re.compile('(multiply|add)\(.*,.*\)')

	with open(input_file) as file:
		lines = file.read()

		matches = pattern.findall(lines)

		for match in matches:
			if match == "multiply":
				print("We have a multiplication expression!")
			elif match == "add":
				print("We have an addition expression!")
			else:
				print("</Error>")

	file.close()


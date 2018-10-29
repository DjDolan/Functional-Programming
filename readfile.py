""" 
Reading File Script
"""

import re

def read_file(input_file, exp):

	file = open(input_file)

	pattern = re.compile('(multiply|add)\(.*,.*\)', re.DOTALL)

	for line in file:
		if pattern.search(line):
			exp.append(line.rstrip())
		else:
			print("line does not contain pattern")
			exit(1)

	file.close()
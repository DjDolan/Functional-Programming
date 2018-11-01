import re
from evaluate import *

def isInteger(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

def read_line(line, nod, i):
	#pattern of expression that we are looking for to evaluate
	pattern = re.compile('(multiply|add)\(\d*,\d*\)')

	matches = pattern.finditer(line)

	if isInteger(line):
		return line
	else:
		for match in matches:
			line = evaluate(line, match.group(), nod, match)

		return read_line(line, nod, i+1)

def read_file(input_text, nod, exp, ans):
	
	file = open(input_text)

	for line in file:
		exp.append(line.strip('\n'))
		line = read_line(line, nod, 0)
		ans.append(line.strip('\n'))

	file.close() #closes the file
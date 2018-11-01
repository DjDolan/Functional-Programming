import re
from evaluate import *

def read(input_text, nod, ans):
	#pattern of expression that we are looking for to evaluate
	pattern = re.compile('(multiply|add)\(\d*,\d*\)')

	file = open(input_text)

	#loop through lines of file and keep looping until there
	#is only an integer value that has the result
	for line in file:
		matches = pattern.finditer(line)

	#go through the matches we found
	for match in matches:
		#evaluate until complete
		line = evaluate(line, match.group(), nod, match)

	#check if there needs to be one more step
	if line.find('add') != -1:
		#find new matches
		matches = pattern.finditer(line)

		for match in matches:
			line = evaluate(line, match.group(), nod, match)

	elif line.find('multiply') != -1:
		#find new matches
		matches = pattern.finditer(line)

		for match in matches:
			line = evaluate(line, match.group(), nod, match)	

	ans.append(line)

	file.close() #closes the file
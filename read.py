import re
from evaluate import *

def read(input_text, nod):
	#pattern of expression that we are looking for to evaluate
	pattern = re.compile('(mulitply|add)\(\d*,\d*\)')

	#opens the text file containing the lines of instructions
	with open(input_text) as file:
		line = file.read() #reads the text file

		matches = pattern.finditer(line) #finds the matches in the file

		#loops through the matches and evaluates each one
		for match in matches:
			#if they find the exact match then get the position of
			#the match, the expression, and perform evaluation of it
			#once finished evaluating then replace the expression with
			#the result in the original expression
			if line.find(match.group()) != -1:
				#position = match.start() #the position
				expression = match.group() #the expression
				line = evaluate(line, expression, nod, match) #evaluate function
				print(line)
			#else it cannot find the expression
			else:
				print("</error> : cannot find match")

	file.close() #closes the file
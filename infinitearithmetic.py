from read import *

def main():
	#command line inputs
	txt = "test.txt"
	num_of_digits = 2

	#container for the final answers
	answers = []
	expression = []

	#read expression
	read_file(txt, num_of_digits, expression, answers)

	#print out results
	for n in range(0, len(expression)):
		print(expression[n], '=', answers[n], sep='')

if __name__ == "__main__":
	main()
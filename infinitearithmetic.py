from read import *

def main():
	#command line inputs
	txt = "test.txt"
	num_of_digits = 2

	#container for the final answers
	answers = []

	#read expression
	read(txt, num_of_digits, answers)

	print(answers)

if __name__ == "__main__":
	main()
"""
This file will take in the original expression, the position of internal expression,
the internal expression, and it will evaluate the internals to replace in the original
expression.
"""

from operations import *

#this function makes the operands the same length by appending zeroes
def make_lists_same_length(op1, op2, i):
	#if they are not the same then keep appending '0'
	if i == len(op1): 
		return
	else:
		op2.append(0)
		make_lists_same_length(op1, op2, i+1)

def parse_right(right_exp, r_op, nod, i, tmp_str):
	#base case : when reaches end of left string
	if i == len(right_exp)-1:
		tmp_str += right_exp[i]
		r_op.append(tmp_str[::-1])
		tmp_str = ""
		return
	#if the it reaches the number of digits then
	#append to the left operand list
	elif len(tmp_str) == nod-1:
		tmp_str += right_exp[i]
		r_op.append(tmp_str[::-1])
		tmp_str = ""
		parse_left(right_exp, r_op, nod, i+1, tmp_str)
	#else keep going through the expression
	else:
		tmp_str += right_exp[i]
		parse_left(right_exp, r_op, nod, i+1, tmp_str)	

def parse_left(left_exp, l_op, nod, i, tmp_str):
	#base case : when reaches end of left string
	if i == len(left_exp)-1:
		tmp_str += left_exp[i]
		l_op.append(tmp_str[::-1])
		tmp_str = ""
		return
	#if the it reaches the number of digits then
	#append to the left operand list
	elif len(tmp_str) == nod-1:
		tmp_str += left_exp[i]
		l_op.append(tmp_str[::-1])
		tmp_str = ""
		parse_left(left_exp, l_op, nod, i+1, tmp_str)
	#else keep going through the expression
	else:
		tmp_str += left_exp[i]
		parse_left(left_exp, l_op, nod, i+1, tmp_str)	

def get_operator(exp):
	#get operator
	if exp.find('add') != -1: op = '+'
	elif exp.find('multiply') != -1: op = '*'
	else: 
		print("</error> : cannot find operator")
		return

	return op

#this function will parse the expression and return the parts
def parse_expression(exp, l_op, r_op, op, nod):
	#get '(' and ')'
	left_bracket = exp.find('(')
	right_bracket = exp.find(')')+1
	comma = exp.find(',')
	
	#temporary string
	temporary_string = ""

	#get left operand
	left = exp[left_bracket+1:comma:]
	left = left[::-1]
	parse_left(left, l_op, nod, 0, temporary_string)

	#get right operand
	right = exp[comma+1:right_bracket-1:]
	right = right[::-1]
	parse_right(right, r_op, nod, 0, temporary_string)

#this function will evaluate the internals or any original expression
def evaluate(orig_exp, exp, nod, match):
	#containers for parsed expression
	operator = get_operator(exp)
	left_operand = []
	right_operand = []
	results = []

	#parse the internal expression
	parse_expression(exp, left_operand, right_operand, operator, nod)

	#cast operands to integers
	#find the shorter expression to evaluate properly
	#reverse the list for proper evaluation
	#map the lists to integers for evaluation
	if len(left_operand) < len(right_operand):
		operand1 = list(map(int, right_operand))
		operand2 = list(map(int, left_operand))
	else:
		operand1 = list(map(int, left_operand))
		operand2 = list(map(int, right_operand))

	#make the lists the same length
	make_lists_same_length(operand1, operand2, len(operand2))

	#operate on the expressions
	operate(operator, operand1, operand2, results, nod)

	#change the expression to results in the original expression
	if orig_exp.find(match.group()) != -1:
		orig_exp = orig_exp.replace(match.group(), str(results[0]))

	return orig_exp
	
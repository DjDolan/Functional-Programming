"""
Parse Expression Script
"""

from evaluate import *

#this function will split the operand according
#to the number of digits specified
def parse_left_operand(left_str, tmp_str, left_op, nod, i):
	#base case
	#if it reaches the end then return
	if i == len(left_str)-1:
		tmp_str += left_str[i]
		left_op.append(tmp_str[::-1])
	#if it reaches the number of digits then append
	elif len(tmp_str) == nod-1:
		tmp_str += left_str[i]
		left_op.append(tmp_str[::-1])
		tmp_str = ""
		parse_left_operand(left_str, tmp_str, left_op, nod, i+1)
	#else it keeps appending to temporary string
	else:
		tmp_str += left_str[i]
		parse_left_operand(left_str, tmp_str, left_op, nod, i+1)

#this function will split the operand according
#to the number of digits specified
def parse_right_operand(right_str, tmp_str, right_op, nod, i):
	#base case
	#if it reaches the end then return
	if i == len(right_str)-1:
		tmp_str += right_str[i]
		right_op.append(tmp_str[::-1])
	#if it reaches the number of digits then append
	elif len(tmp_str) == nod-1:
		tmp_str += right_str[i]
		right_op.append(tmp_str[::-1])
		tmp_str = ""
		parse_left_operand(right_str, tmp_str, right_op, nod, i+1)
	#else it keeps appending to temporary string
	else:
		tmp_str += right_str[i]
		parse_left_operand(right_str, tmp_str, right_op, nod, i+1)

#this function will clean the expression
#for easier evaluation
def strip_expression(exp):
	#remove beginning
	if exp.find('multiply') != -1:
		exp = exp.replace('multiply', '')
	elif exp.find('add') != -1:
		exp = exp.replace('add', '')
	else:
		print("unexpected error")
		exit(1)

	return exp

#function will divide the expression to
#pass for evaluation
def read_expression(exp, nod, results):
	#temporary variable
	temporary_string = ""
	left_operand = []
	right_operand = []

	#get operator
	if exp.find('multiply') != -1: 
		op = '*'
	elif exp.find('add') != -1: 
		op = '+'
	else:
		print("unexpected error")
		exit(1)

	#strip expression of impurities
	exp = strip_expression(exp)

	#split the expression to left and right
	left_string = exp[exp.find('(')+1:exp.find(','):]
	if not left_string:
		print("</error> cannot parse empty string <", exp, ">", sep='')
		results.append(-1)
		return
	else:
		parse_left_operand(left_string[::-1], temporary_string, left_operand, nod, 0)

	right_string = exp[exp.find(',')+1:exp.find(')'):]
	if not right_string:
		print("</error> cannot parse empty string <", exp, ">", sep='')
		results.append(-1)
		return
	else:
		parse_right_operand(right_string[::-1], temporary_string, right_operand, nod, 0)

	#evaluate the expression
	evaluate(left_operand, right_operand, nod, op, results)

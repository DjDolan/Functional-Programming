"""
This file will contain the necessary functions to evaluate expressions.
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


#this function evaluates the expression by the operation
def evaluate(left, right, nod, op, results):
	#temporary containers
	res = []

	#find the shorter expression to evaluate properly
	#reverse the list for proper evaluation
	#map the lists to integers for evaluation
	if len(left) < len(right):
		operand1 = list(map(int, right))
		operand2 = list(map(int, left))
	else:
		operand1 = list(map(int, left))
		operand2 = list(map(int, right))

	#pass to make_list_same_length function
	make_lists_same_length(operand1, operand2, len(operand2))

	#operate on the operands with Operations.py
	if op == '+':
		#if operator is add then call the add function
		add(operand1, operand2, res, nod, 0)
		results.append(sum(res))
	elif op == '*':
		#if operator is multiply call the multiply function
		multiply(operand1, operand2, res, nod, 0, 0)
		results.append(sum(res))

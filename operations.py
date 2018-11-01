"""
This file will contain the necessary functions to perform operations
on the arithmetic expressions.
"""

#this function will take each element, find its place value, and add them
def add(op1, op2, res, nod, i):
	#takes element at 'i' and adds both from
	#each operand and multiplies by 10^(i * nod)
	#stores in results container and returns
	if i == len(op2)-1:
		_sum = (op1[i] + op2[i]) * (10 ** (i * nod))
		res.append(_sum)
	else:
		_sum = (op1[i] + op2[i]) * (10 ** (i * nod))
		res.append(_sum)
		add(op1, op2, res, nod, i+1)

	return res	

#this function will take each element, find its place value, and multiply them
#to the elements found in the second list
def multiply(op1, op2, res, nod, i, j):
	#variables for easier calculations
	i_place_value = 10 ** (i * nod)
	j_place_value = 10 ** (j * nod)

	#'i' is the first operand iterator
	if i == len(op1)-1:	
		#'j' is the second operand iterator
		#nested if recursion that checks if 'j' has reached the end
		#after iterating through the first operand
		if j == len(op2)-1:
			_prod = (op1[i] * i_place_value) * (op2[j] * j_place_value)
			res.append(_prod)
		else:
			_prod = (op1[i] * i_place_value) * (op2[j] * j_place_value)
			res.append(_prod)
			multiply(op1, op2, res, nod, 0, j+1)
	#if operand1 has not reach the end then calculate and iterate
	#forward through the expression
	else:
		_prod = (op1[i] * i_place_value) * (op2[j] * j_place_value)
		res.append(_prod)
		multiply(op1, op2, res, nod, i+1, j)

def operate(op, left, right, results, nod):
	#temporary results container for inner results
	res = []

	if op == '+':
		add(left, right, res, nod, 0)
		results.append(sum(res))

	elif op == '*':
		multiply(left, right, res, nod, 0, 0)
		results.append(sum(res))

	else:
		print("</error> : no operator")
		exit(1)

from operator import add, sub, mul

def multiplyByFive(x):
	"""
	This function should take in the variable x and return a number five times greater than x. 
	Use built-in/primitive operators. Use only one line. 
	Examples:
	-multiplyByFive(2) returns 10
	-multiplyByFive(3) returns 15
	-multiplyByFive(10) returns 50
	"""
	"""YOUR CODE HERE"""
	return x * 5

def summer(x, y):
	"""
	This function should take in the variables x and y and return the sum. 
	Use built-in/primitive operators. Use only one line. 
	Examples:
	-summer(1, 2) returns 3
	-summer(-1, 9) returns 8
	-summer(0, 0) returns 0
	"""
	"""YOUR CODE HERE"""
	return x + y

def divisionByFour(x):
	"""
	This function returns both true division and floor division of x by 4. 
	Use only one line. 
	Examples:
	-divisionByFour(4) returns 1, 1
	-divisionByFour(8) returns 2, 2
	-divisionByFour(9) returns 2.25, 2
	"""
	"""YOUR CODE HERE"""
	return x / 4, x // 4

def addFiveSubTwoMulThree(x):
	"""
	This function should take in the variable x. It first adds five, then subtracts two, then multiplies by three. It then returns the result. 
	Use the functions from the math library. Use only one line. 
	In case you've forgotten, "from math import add, sub, mul" means "From the math library, I want the add, sub, and mul functions". If you
	don't know how to use these functions, look them up. 

	Examples:
	-addFiveSubTwoMulThree(1) returns 12
	-addFiveSubTwoMulThree(2) returns 15
	-addFiveSubTwoMulThree(10) return 39
	"""
	"""YOUR CODE HERE"""
	return mul(sub(add(x, 5), 2), 3)

def multiplySums(a, b, c, d):
	"""
	This function takes in four integers. It multiplies the sum of a and b with the sum of c and d. 
	Use the functions from the math library. Use only one line. 
	Examples:
	-multiplySums(1, 2, 3, 4) returns 21
	-multiplySums(1, 3, 2, 4) returns 24
	-multiplySums(1, 4, 3, 2) returns 25
	"""
	"""YOUR CODE HERE"""
	return mul(add(a, b), add(c, d))

def greaterThanZero(x):
	"""
	This function returns whether x is greater than zero. 
	Use only one line if possible. 
	Examples:
	-greaterThanZero(2) returns True
	-greaterThanZero(-1) returns False
	-greaterThanZero(0) returns False
	"""
	"""YOUR CODE HERE"""
	return x > 0

def printAndReturn():
	"""
	This function should print the words "Hi there!" and return the words "Goodbye!"
	"""
	"""YOUR CODE HERE"""
	print("Hi there!")
	return "Goodbye!"
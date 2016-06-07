from hw import *

# Test multiplyByFive
if multiplyByFive(2) == 10 and multiplyByFive(3) == 15 and multiplyByFive(4) == 20 and multiplyByFive(10) == 50:
	print("multiplyByFive passed all tests!")
else:
	print("multiplyByFive failed some tests")

# Test summer
if summer(1, 2) == 3 and summer(-1, 9) == 8 and summer (0, 0) == 0 and summer(29, 1) == 30:
	print("summer passed all tests!")
else:
	print("summer failed some tests")

# test divisionByFour
values = [4, 8, 9]
answers = [[1, 1], [2, 2], [2.25, 2]]
print("divisionByFour results (three tests total):")
for i in range(len(values)):
	x = values[i]
	answer = answers[i]
	first, second = divisionByFour(x)
	if first == answer[0] and second == answer[1]:
		print("pass")
	else:
		print("fail")

# test addFiveSubTwoMulThree
values = [1, 2, 10]
answers = [12, 15, 39]
print("addFiveSubTwoMulThree results (three tests total):")
for i in range(len(values)):
	x = values[i]
	answer = answers[i]
	trial = addFiveSubTwoMulThree(x)
	if trial == answer:
		print("pass")
	else:
		print("fail")

# test multiplySums
if multiplySums(1, 2, 3, 4) == 21 and multiplySums(1, 3, 2, 4) == 24 and multiplySums(1, 4, 3, 2) == 25:
	print("multiplySums passed all tests!")
else:
	print("multiplySums failed some tests")

# test greaterThanZero
if greaterThanZero(2) == True and greaterThanZero(-1) == False and greaterThanZero(0) == False:
	print("greaterThanZero passed all tests!")
else:
	print("greaterThanZero failed some tests")

# test printAndReturn
print(printAndReturn())
print('If the above has both "Hi there!"" and "Goodbye!", you passed all tests!')
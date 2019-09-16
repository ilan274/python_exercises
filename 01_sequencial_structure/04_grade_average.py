# Create a program that asks 4 bi-monthly grades and displays the average

def isFloat(x):
	return x % 1 != 0
#if true, number is float

grade1 = float(input("Please, type the first grade: "))
grade2 = float(input("Please, type the second grade: "))
grade3 = float(input("Please, type the third grade: "))
grade4 = float(input("Please, type the fourth grade: "))

average = (grade1 + grade2 + grade3 + grade4) / 4

if isFloat(average):	# if number have decimals, print with them
	print("The average grade is {:.2f}.".format(average))
else:					# else, don't print with decimals
	print("The average grade is {:.0f}.".format(average))

# Make a program that asks how much you earn per hour and the number of hours
# worked in the last month, then Calculate and show your total salary for that month

def isFloat(x):
	return x % 1 != 0
#if true, number is float


per_hour = float(input("How much you earn per hour? "))
hours_worked = float(input("How many hours did you work in the last month? "))

salary = per_hour * hours_worked

if isFloat(salary):	#verify if contains decimals
	print("The total salary in the last month was ${:.2f}".format(salary))
else:				#return number without decimals
	print("The total salary in the last month was ${:.0f}".format(salary))
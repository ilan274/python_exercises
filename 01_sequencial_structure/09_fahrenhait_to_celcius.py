# Make a Program that asks for temperature
# in Fahrenheit and displays the temperature in Celsius

def isFloat(x):
	return x % 1 != 0
#if true, number is float

try:				# will try to execute the next block of statements
	fahrenheit = float(input("Please enter how many degrees in fahrenheit: "))
	fahr_to_cel = (5 * (fahrenheit - 32) / 9)
	if isFloat(fahr_to_cel):
		print("º{:.2f} Fahrenheit is equal to {:.2f}º Celcius".format(fahrenheit, fahr_to_cel))
	else:
		print("º{:.0f} Fahrenheit is equal to {:.0f}º Celcius".format(fahrenheit, fahr_to_cel))
except ValueError:	# handeling an error, if found
	print("Please enter only whole numbers.")


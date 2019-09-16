# Make a Program that asks for temperature
# in Celcius and displays the temperature in Fahrenheit.

def isFloat(x):
	return x % 1 != 0
#if true, number is float

try:				# will try to execute the next block of statements
	celcius = float(input("Please enter how many degrees in celcius: "))
	cel_to_fahr = ((celcius * (9/5)) + 32)
	if isFloat(cel_to_fahr):
		print("º{:.2f} Celcius is equal to º{:.2f} Fahrenheit".format(celcius, cel_to_fahr))
	else:
		print("º{:.0f} Celcius is equal to º{:.0f} Fahrenheit".format(celcius, cel_to_fahr))
except ValueError:	# handeling an error, if found
	print("Please enter only whole numbers.")
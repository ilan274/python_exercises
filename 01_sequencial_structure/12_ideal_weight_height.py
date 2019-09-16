# Having as input a person's height, create an algorithm
# that calculates their ideal weight using the following
# formula: (72.7 * height) - 58

def isFloat(x):
	return x % 1 != 0
#if true, number is float

try:
	height = float(input("Enter your height: "))
	calc = (72.7 * height) - 58
	if isFloat(calc):	# verify if number have decimals
		print("Your ideal weight is: {:.2f}.".format(calc))
	else:				# if not, returns number with no decimals
		print("Your ideal weight is: {:.0f}.".format(calc))

except ValueError:
	print("Only numbers, please.")

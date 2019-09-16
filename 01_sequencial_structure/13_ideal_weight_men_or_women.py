# Having as input a person's height, create an algorithm
# that calculates their ideal weight using the following
# formulas;
# Men: 		(72.7 * height) - 58
# Women:	(62.1 * height) - 44.7

def isFloat(x):
	return x % 1 != 0
# returns true if number is float (contains decimal places)

men_or_women = input("Are you man or woman? ")

if men_or_women == "man" or men_or_women == "men":
	# returns true if user types either 'man' or 'men'
	height = float(input("Enter your height: "))
	calc = (72.7 * height) - 58
	if isFloat(calc):	# verify if number have decimals
		print("Your ideal weight is: {:.2f}.".format(calc))
	else:				# if not, returns number with no decimals
		print("Your ideal weight is: {:.0f}.".format(calc))
elif men_or_women == "woman" or men_or_women == "women":
	# returns true if user types either 'woman' or 'women'
	height = float(input("Enter your height: "))
	calc = (62.1 * height) - 44.7
	if isFloat(calc):	# verify if number have decimals
		print("Your ideal weight is: {:.2f}.".format(calc))
	else:				# if not, returns number with no decimals
		print("Your ideal weight is: {:.0f}.".format(calc))
else:
	print("Please type \"man\" or \"woman\".")
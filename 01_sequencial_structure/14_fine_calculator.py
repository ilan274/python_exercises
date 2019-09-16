# John bought a computer to control the daily income of his work.
# Every time he brings a fish weight higher than that established by the
# fishing regulation of the state of Sao Paulo, which is 50kg, he must
# pay a fine of $ 4.00 per excess kg. John needs you to make a program
# that reads the weight variable (fish weight) and calculates the excess.
# Record in the excess variable the number of kg over the limit and in
# the fine variable the amount of the fine that John must pay. Print the
# program data with the appropriate messages.

def isFloat(x):
	return x % 1 != 0
#if true, number is is float (contains decimal places)

fish_weight = float(input("How many kilos did you catch? "))

if fish_weight > 50:			# checks if fishing exceeded 50kg
	fine = (fish_weight - 50) * 4
	diference = fish_weight - 50
	if isFloat(fish_weight):	# checks if the number has decimal places
		print("Since your fishing exceeded 50kg (total: {}), you'll pay a fine of ${:.2f}.".format(fish_weight, fine))
		print("{:.2f} x 4 = ${:.2f}".format(diference, fine))
	else:
		print("Since your fishing exceeded 50kg (total: {}), you'll pay a fine of ${:.0f}.".format(fish_weight, fine))
		print("{:.0f} x 4 = ${:.0f}".format(diference, fine))
else:							# if didn't exceed 50kg
	print("You won't pay any fine since you didn't exceed 50kg")

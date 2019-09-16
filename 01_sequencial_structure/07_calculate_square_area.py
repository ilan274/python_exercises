# Make a program that calculates the area of a square, then shows twice that area to the user

square_size = float(input("How many meters does one size has: "))

square_size = square_size * square_size

square_double = square_size * 2

print("The square area size is {:.2f} and the double is {:.2f}".format(square_size, square_double))
# Make a program that asks for two integers and a real number than calculate and show:
# The product of double the first with half of the second;
# The sum of the triple of the first with the third;
# The third cubed.

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = float(input("Enter a real(float) number: "))

first_calc = (first * 2) + (second / 2)
second_calc = (first * 3) + third
third_calc = third ** 3

print("The product of double the first with half of the second is {}.".format(first_calc))
print("The sum of the triple of the first with the third is {}.".format(second_calc))
print("The third cubed is {}.".format(third_calc))
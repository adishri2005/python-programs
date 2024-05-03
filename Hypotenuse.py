#WAP to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.

print("FINDING THE LENGTH OF THE HYPOTENUSE OF A RIGHT TRIANGLE")
a = float(input("Enter the length of the first side of the triangle:"))       #taking input from the user
b = float(input("Enter the length of the second side of the triangle:"))      #taking input from the user
c = (a**2 + b**2)**0.5                                                        #computing the length of the hypotenuse
print("The length of the hypotenuse of the right triangle is:",c)             #printing the length of the hypotenuse
#In this program, we have taken the lengths of the two sides of the right triangle as input from the user.
#The length of the hypotenuse is calculated using the Pythagoras theorem.
#The length of the hypotenuse is then printed.

#Pythagoras theorem says that in a right-angled triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.
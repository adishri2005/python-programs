#WAP a to find area of triangle when length of sides are given.

print("FINDING THE AREA OF A TRIANGLE")
a = float(input("Enter the length of the first side of the triangle:"))       #taking input from the user
b = float(input("Enter the length of the second side of the triangle:"))      #taking input from the user
c = float(input("Enter the length of the third side of the triangle:"))       #taking input from the user
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is:",area)             #printing the area of the triangle 

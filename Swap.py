#WAP to swap two numbers without taking additional variable.

print("SWAPPING TWO NUMBERS WITHOUT TAKING ADDITIONAL VARIABLE")

print("Enter the first number:")
a = int(input())                #taking input from the user
print("Enter the second number:")
b = int(input())                #taking input from the user

a = a + b                       #swapping the numbers
b = a - b
a = a - b

print("The first number after swapping is:",a)   #printing the first number after swapping
print("The second number after swapping is:",b)  #printing the second number after swapping


#WAP to find the factorial of a given number 
print("FINDING FACTORIAL OF A NUMBER")
print("Enter the number to find the factorial:")
num = int(input())                                       #taking input from the user
fact = 1                                                 #initializing the factorial
for i in range(1,num+1):                                 #loop to find the factorial
    fact = fact * i                                      #finding the factorial
print("The factorial of the given number is = ",fact)    #printing the factorial


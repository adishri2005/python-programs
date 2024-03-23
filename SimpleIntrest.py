# WAP to calculate the Simple Intrerest

print("CALCULATING SIMPLE INTEREST")

p = float(input("Enter the principal amount: ")) #taking input from the user
r = float(input("Enter the rate of interest: ")) #taking input from the user
t = float(input("Enter the time period: "))      #taking input from the user

si = (p*r*t)/100                                #calculating the simple interest
print("The simple interest is:",si)             #printing the simple interest

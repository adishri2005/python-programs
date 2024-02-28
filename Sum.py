#WAP to print sum of digits
print("FINDING SUM OF DIGITS")
print("Enter the number to find the sum of digits:")
num = int(input())                                       #taking input from the user
sum = 0                                                  #initializing the sum variable to 0
while num > 0:                                           #loop to find the sum of digits
    sum += num % 10                                        #adding the last digit of the number to the sum
    num = num // 10                                        #removing the last digit from the number
print("The sum of digits is:",sum)                       #printing the sum of digits


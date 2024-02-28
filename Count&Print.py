#WAP to print all numbers divisible by 5 or 7 between 1 to 100
print("FINDING ALL NUMBERS DIVISIBLE BY 5 OR 7 BETWEEN 1 TO 100")
for i in range(1,101):                                      #iterating through the range of numbers
    if i%5 == 0 or i%7 == 0:                                  #checking whether the number is divisible by 5 or 7
        print(i)                                              #printing the numbers
        
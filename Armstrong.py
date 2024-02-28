#WAP to find whether a given number is an Armstrong number or not
print("FINDING WHETHER A NUMBER IS ARMSTRONG OR NOT")
print("Enter the number to find whether it is an Armstrong number or not:")
num = int(input())                                       #taking input from the user
sum = 0                                                  #initializing the sum
temp = num                                               #storing the number in a temporary variable
while temp > 0:                                          #loop to find the sum of the cubes of the digits
    digit = temp % 10                                    #finding the last digit of the number
    length = len(str(num))                               #finding the number of digits in the number                                  
    sum += digit ** length                               #finding the sum of the cubes of the digits
    temp //= 10
if num == sum:                                           #checking whether the number is an Armstrong number or not
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

    

    
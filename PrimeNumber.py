#WAP to find whether a given number is a prime number or not
print("FINDING WHETHER A NUMBER IS PRIME OR NOT")
print("Enter the number to find whether it is a prime number or not:")
num = int(input())                                       #taking input from the user
if num > 1:                                              #checking whether the number is greater than 1
    for i in range(2,num):                               #loop to find whether the number is prime or not
        if num % i == 0:                                  #checking whether the number is divisible by any other number
            print(num,"is not a prime number")            #printing the result
            break                                         #breaking the loop
    else:                                                #executing when the loop is not broken
        print(num,"is a prime number")                    #printing the result
else:
    print(num,"is not a prime number")                    #printing the result

#WAP to find prime numbers in a given range of 1 to 100
print("FINDING PRIME NUMBERS IN A GIVEN RANGE OF 1 TO 100")
print ("Enter the range of numbers to find the prime numbers in the range of 1 to 100:")
n = int(input())                                            #taking input from the user
for i in range(2,n+1):                                      #iterating through the range of numbers
    for j in range(2,i):                                    #iterating through the range of numbers
        if i%j == 0:                                         #checking whether the number is prime or not
            break
    else:
        print(i)                                             #printing the prime numbers

        
#WAP to find Fibbinacci series upto n terms
print("FINDING FIBONACCI SERIES")
print("Enter the number of terms for the Fibonacci series:")
n = int(input())                                          #taking input from the user
a = 0                                                     #initializing the first term
b = 1                                                     #initializing the second term
print("The Fibonacci series is :")
print(a)                                                  #printing the first term
print(b)                                                  #printing the second term
for i in range(2,n):                                      #loop to find the Fibonacci series
    c = a + b                                             #finding the next term
    print(c)                                              #printing the next term
    a = b                                                 #swapping the values
    b = c                                                 #swapping the values

    
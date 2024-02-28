#WAP to print the table of a given number
print("PRINTING THE TABLE OF A GIVEN NUMBER")
print("Enter the number to print the table of:")
num = int(input())                                       #taking input from the user
print("The table of",num,"is:")                                
for i in range(1,11):                                    #loop to print the table of the number
    print(num,"*",i,"=",num*i)                              #printing the table of the number

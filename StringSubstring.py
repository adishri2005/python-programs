#WAP to enter a string and a substring. We have to print the number of times the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left.

print("FINDING THE NUMBER OF TIMES A SUBSTRING OCCURS IN A GIVEN STRING")
print("Enter the string:")
string = input()                                          #taking input from the user
print("Enter the substring:")
substring = input()                                       #taking input from the user
count = 0                                                 #initializing the count variable to 0
for i in range(len(string)):                               #iterating through the string
    if string[i:i+len(substring)] == substring:             #checking whether the substring occurs in the string or not
        count += 1                                            #incrementing the count variable
print("The number of times the substring occurs in the string are:",count)  #printing the number of times the substring occurs in the string

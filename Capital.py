#WAP to count and display the number of capital letters in a given string
print("COUNTING AND DISPLAYING THE NUMBER OF CAPITAL LETTERS IN A GIVEN STRING")
print("Enter the string to count and display the number of capital letters in the string:")
string = input()                                          #taking input from the user
count = 0                                                 #initializing the count variable to 0
for i in string:                                          #iterating through the string
    if i.isupper():                                         #checking whether the character is a capital letter or not
        count += 1                                            #incrementing the count variable
print("The number of capital letters in the string are:",count)  #printing the number of capital letters in the string

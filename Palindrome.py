#WAP to find whether a given string is a palindrome or not
print("FINDING WHETHER A STRING IS PALINDROME OR NOT")
print("Enter the string to find whether it is a palindrome or not:")
string = input()                                          #taking input from the user
if string == string[::-1]:                                 #checking whether the string is a palindrome or not
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")                    #printing the result
    
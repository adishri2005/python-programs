#WAP using membership operator find whether a given character is in a string.

print("FINDING WHETHER A CHARACTER IS IN A STRING OR NOT")
print("Enter the character to find whether it is in the string:")
char = input()                                       #taking input from the user
string = "Hello, World!"                             #string
if char in string:                                   #using membership operator to check whether the character is in the string or not
    print(char,"is in the string")
else:
    print(char,"is not in the string")

    
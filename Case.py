#WAP to convert all lowercase letters to uppercase and vice versa in a given string
print("CONVERTING ALL LOWERCASE LETTERS TO UPPERCASE AND VICE VERSA")
print("Enter the string to convert all lowercase letters to uppercase and vice versa:")
string = input()                                          #taking input from the user
new_string = ""                                          #initializing the new_string variable to an empty string
for i in string:                                         #iterating through the string
    if i.islower():                                      #checking whether the letter is lowercase
        new_string += i.upper()                           #converting the letter to uppercase and adding it to the new_string
    elif i.isupper():                                    #checking whether the letter is uppercase
        new_string += i.lower()                           #converting the letter to lowercase and adding it to the new_string
    else:
        new_string += i                                   #adding the letter to the new_string
print("The new string is:",new_string)                  #printing the new string

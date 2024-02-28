#WAP to count total number of vowels in a given string
print("COUNTING TOTAL NUMBER OF VOWELS IN A GIVEN STRING")
print("Enter the string to count the total number of vowels in the string:")
string = input()                                          #taking input from the user
count = 0                                                 #initializing the count variable to 0
for i in string:                                          #iterating through the string
    if i in "aeiouAEIOU":                                   #checking whether the character is a vowel or not
        count += 1                                            #incrementing the count variable
print("The total number of vowels in the string are:",count)  #printing the total number of vowels in the string

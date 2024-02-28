#WAP to count the number of occurences of each alphabet (case insensitive)and display the same when given a string containing both upper and lower case alphabet
print("COUNTING THE NUMBER OF OCCURENCES OF EACH ALPHABET (CASE INSENSITIVE)")
print("Enter the string to count the number of occurences of each alphabet in the string:")
string = input()                                          #taking input from the user
count = {}                                                #initializing the count dictionary
for i in string:                                          #iterating through the string
    if i.isalpha():                                         #checking whether the character is an alphabet or not
        if i in count:                                         #checking whether the alphabet is already present in the dictionary or not
            count[i] += 1                                        #incrementing the count of the alphabet
        else:
            count[i] = 1                                         #initializing the count of the alphabet
print("The number of occurences of each alphabet in the string are:")
for i in count:                                           #iterating through the dictionary
    print(i,":",count[i])                                    #printing the number of occurences of each alphabet in the string

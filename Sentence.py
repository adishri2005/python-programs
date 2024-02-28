#WAP to input a sentence and print words in different lines
print("PRINTING WORDS IN DIFFERENT LINES")
print("Enter the sentence to print the words in different lines:")
sentence = input()                                          #taking input from the user
print("The words in the sentence are:")
for i in sentence.split():                                  #iterating through the sentence
    print(i)                                                  #printing the words in different lines



#WAP to input a sentence and print the words in reverse order
print("PRINTING THE WORDS IN REVERSE ORDER")
print("Enter the sentence to print the words in reverse order:")    
sentence = input()                                          #taking input from the user
print("The words in the sentence in reverse order are:")
for i in sentence.split()[::-1]:                            #iterating through the sentence in reverse order
    print(i)                                                  #printing the words in reverse order
    
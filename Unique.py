#WAP to count number of unique words in a given sentence using sets
print("COUNTING NUMBER OF UNIQUE WORDS IN A GIVEN SENTENCE")
print("Enter the sentence to count the number of unique words in the sentence:")
sentence = input()                                        #taking input from the user
words = sentence.split()                                  #splitting the sentence into words
unique_words = set(words)                                 #converting the list of words into a set of unique words
print("The number of unique words in the sentence are:",len(unique_words))  #printing the number of unique words in the sentence

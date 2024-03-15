#WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.

print("FINDING THE SCORE OF THE RUNNER-UP")
n = int(input("Enter the number of students:"))  #taking input from the user
scores = []                                      #creating an empty list scores
for i in range(n):
    score = int(input())                         #taking input from the user
    scores.append(score)                         #appending the score to the list scores
scores.sort()                                    #sorting the list scores
print("The score of the runner-up is:",scores[-2])  #printing the score of the runner-up

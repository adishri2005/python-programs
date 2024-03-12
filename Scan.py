#WAP to scan n values in range 0-3 and print the number of times each value has occurred.  

print("SCANNING N VALUES IN RANGE 0-3 AND PRINTING THE NUMBER OF TIMES EACH VALUE HAS OCCURRED")
n = int(input("Enter the number of values to scan:"))  #taking input from the user
count = [0,0,0,0]                                      #creating a list count to store the count of each value
for i in range(n):
    value = int(input())                               #taking input from the user
    count[value] += 1                                  #incrementing the count of the value
print("The number of times 0 has occurred is:",count[0])  #printing the count of 0
print("The number of times 1 has occurred is:",count[1])  #printing the count of 1
print("The number of times 2 has occurred is:",count[2])  #printing the count of 2
print("The number of times 3 has occurred is:",count[3])  #printing the count of 3

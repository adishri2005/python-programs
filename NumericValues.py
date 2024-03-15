#Create a tuple to store n numeric values and find average of all values.

print("CREATING A TUPLE TO STORE N NUMERIC VALUES AND FINDING THE AVERAGE OF ALL VALUES")
n = int(input("Enter the number of values to store in the tuple:"))    #taking input from the user    
values = ()                                                            #creating an empty tuple values
for i in range(n):
    value = int(input("Enter the value:"))                             #taking input from the user
    values += (value,)                                                 #appending the value to the tuple values
average = sum(values)/n                                                #finding the average of all values
print("The average of all values is:",average)                         #printing the average of all values
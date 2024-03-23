#WAP to convert given seconds into hours, minutes and remaining seconds.

print("CONVERTING SECONDS INTO HOURS, MINUTES AND REMAINING SECONDS")

seconds = int(input("Enter the number of seconds:"))       #taking input from the user

hours = seconds // 3600                                    #finding the number of hours
minutes = (seconds % 3600) // 60                          #finding the number of minutes
remaining_seconds = (seconds % 3600) % 60                 #finding the remaining seconds

print("The number of hours is:",hours)                     #printing the number of hours
print("The number of minutes is:",minutes)                 #printing the number of minutes
print("The number of remaining seconds is:",remaining_seconds) #printing the remaining seconds


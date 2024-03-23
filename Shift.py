#WAP to find left shift and right shift values of a given number.

print("FINDING LEFT SHIFT AND RIGHT SHIFT VALUES OF A NUMBER")

num = int(input("Enter the number:"))       #taking input from the user
left_shift = num << 1                       #left shift operation
right_shift = num >> 1                      #right shift operation
print("The left shift value of the given number is:",left_shift)  #printing the left shift value
print("The right shift value of the given number is:",right_shift) #printing the right shift value


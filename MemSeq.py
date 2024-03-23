#WAP Using membership operator find whether a given number is in sequence (10,20,56,78,89)

print("FINDING WHETHER A NUMBER IS IN A SEQUENCE OR NOT")
print("Enter the number to find whether it is in the sequence (10,20,56,78,89):")
num = int(input())                                       #taking input from the user
if num in [10,20,56,78,89]:                              #using membership operator to check whether the number is in the sequence or not
    print(num,"is in the sequence")
else:
    print(num,"is not in the sequence")

    
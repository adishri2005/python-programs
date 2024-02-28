#WAP to create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#a) Fruits which are in both sets s1 and s2
#b) Fruits only in s1 but not in s2
#c) Count of all fruits from s1 and s2

print("CREATING 2 SETS OF FRUITS AND FINDING THE INTERSECTION, DIFFERENCE AND COUNT OF FRUITS")
n = int(input("Enter the number of fruits in each set:"))  #taking input from the user
s1 = set()                                                 #creating an empty set s1
s2 = set()                                                 #creating an empty set s2
print("Enter the fruits for set 1:")                      #taking input from the user
for i in range(n):
    s1.add(input())                                        #adding the fruits to the set s1
print("Enter the fruits for set 2:")                      #taking input from the user
for i in range(n):
    s2.add(input())                                        #adding the fruits to the set s2
print("The fruits which are in both sets 1 and 2 are:",s1.intersection(s2))  #finding the intersection of the sets s1 and s2
print("The fruits only in 1 but not in 2 are:",s1.difference(s2))            #finding the difference of the sets s1 and s2
print("The count of all fruits from 1 and 2 is:",len(s1.union(s2)))          #finding the count of all fruits from the sets s1 and s2

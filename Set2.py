#WAP to take two sets and apply various set operations on them :
#S1 = {Red ,yellow, orange , blue }
#S2 = {violet, blue , purple}

print("CREATING 2 SETS AND APPLYING VARIOUS SET OPERATIONS ON THEM")
S1 = {"Red","yellow","orange","blue"}  #creating set S1
S2 = {"violet","blue","purple"}        #creating set S2
print("The set S1 is:",S1)             #printing the set S1
print("The set S2 is:",S2)             #printing the set S2

print("The union of the sets S1 and S2 is:",S1.union(S2))  #finding the union of the sets S1 and S2
print("The intersection of the sets S1 and S2 is:",S1.intersection(S2))  #finding the intersection of the sets S1 and S2
print("The difference of the sets S1 and S2 is:",S1.difference(S2))    #finding the difference of the sets S1 and S2
print("The symmetric difference of the sets S1 and S2 is:",S1.symmetric_difference(S2))  #finding the symmetric difference of the sets S1 and S2
print("The count of all fruits from 1 and 2 is:",len(S1.union(S2)))  #finding the count of all fruits from the sets S1 and S2

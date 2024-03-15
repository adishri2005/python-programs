#Create a dictionary of n persons where key is name and value is city.
#a) Display all names
#b) Display all city names
#c) Display student name and city of all students.
#d) Count number of students in each city.

print("CREATING A DICTIONARY OF N PERSONS WHERE KEY IS NAME AND VALUE IS CITY")
n = int(input("Enter the number of persons:"))                                      #taking input from the user
print()                                      
persons = {}                                                                        #creating an empty dictionary persons
for i in range(n):
    name = input("Enter the name of the person:")  
    city = input("Enter the city of the person:")  
    persons[name] = city  
    print()                                                                         #adding the name and city to the dictionary persons
print("The dictionary of persons is:",persons)     
print("The names of the persons are:",persons.keys())  
print("The cities of the persons are:",persons.values())  
print("The names and cities of the persons are:",persons) 
count = {}                                                                          #creating an empty dictionary count
for city in persons.values():
    count[city] = count.get(city,0) + 1                                             #incrementing the count of the city
print("The number of students in each city is:",count)                              #printing the number of students in each city

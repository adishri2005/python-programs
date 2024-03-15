#Store details of n movies in a dictionary by taking input from the user. Each movie
#must store details like name, year, director name, production cost, collection made
#(earning) & perform the following :-
#a) print all movie details
#b) display name of movies released before 2015
#c) print movies that made a profit.
#d) print movies directed by a particular director.

print("STORING DETAILS OF N MOVIES IN A DICTIONARY")
n = int(input("Enter the number of movies:"))                                        #taking input from the user
print()
movies = {}                                                                          #creating an empty dictionary movies
for i in range(n):
    name = input("Enter the name of the movie:")  
    year = int(input("Enter the year of the movie:"))  
    director = input("Enter the director of the movie:")  
    production_cost = float(input("Enter the production cost of the movie:"))  
    collection = float(input("Enter the collection made by the movie:"))  
    movies[name] = [year,director,production_cost,collection]  
    print()                                                                           #adding the details of the movie to the dictionary movies

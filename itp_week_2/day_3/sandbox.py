# ITP Week 2 Day 3 (In-Class) Practice

#Our Data
my_movies = ["The Godfather", "Ace Ventura", "Gigli", "Die Hard"]

new_releases = ["Encino Man", "I know what you did last Summer", "Phantom Menace"]


#Function BODY
def update_movies(movies):

    for movie in movies:

        my_movies.append(movie)


#Function CALL
update_movies(new_releases)

print(my_movies)

# # 5. Movie Recommendation System
# ### Problem Statement
# A streaming platform stores movie information.
# Each movie contains
# * Movie ID
# * Title
# * Genre
# * Rating
# * Watch Count
# ### Requirements
# 1. Fetch all movies.
# 2. Sort movies based on Rating.
# 3. Search a movie using Movie ID.
# 4. Display Top 10 highest-rated movies.
# 5. Display the most watched movie in every genre.
# ### Concepts
# * Sorting
# * Searching
# * Dictionaries
# * SQL GROUP BY

import sqlite3


class Movie:

    def __init__(self, movie_id, title, genre, rating, watch_count):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watch_count = watch_count


def create_database():

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            movie_id INTEGER PRIMARY KEY,
            title TEXT,
            genre TEXT,
            rating REAL,
            watch_count INTEGER
        )
    """)

    cursor.execute("DELETE FROM movies")

    movies = [
        (1, "Inception", "Sci-Fi", 8.8, 1200),
        (2, "The Matrix", "Sci-Fi", 8.7, 1500),
        (3, "Interstellar", "Sci-Fi", 8.9, 1100),
        (4, "The Dark Knight", "Action", 8.5, 1600),
        (5, "Mad Max", "Action", 8.1, 1300),
        (6, "Gladiator", "Action", 8.6, 1400),
        (7, "Titanic", "Romance", 7.8, 1800),
        (8, "La La Land", "Romance", 8.0, 1700),
        (9, "The Notebook", "Romance", 7.9, 1900),
        (10, "Parasite", "Thriller", 8.4, 1250),
        (11, "Se7en", "Thriller", 8.3, 1350),
        (12, "Gone Girl", "Thriller", 8.2, 1450)
    ]

    cursor.executemany(
        "INSERT INTO movies VALUES (?,?,?,?,?)",
        movies
    )

    conn.commit()
    conn.close()


def fetch_movies():

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    movie_list = []
    for row in rows:
        movie = Movie(row[0], row[1], row[2], row[3], row[4])
        movie_list.append(movie)

    conn.close()
    return movie_list


def bubble_sort(movies):

    n = len(movies)
    for i in range(n):
        for j in range(n - i - 1):
            if movies[j].rating < movies[j + 1].rating:
                movies[j], movies[j + 1] = movies[j + 1], movies[j]

    return movies


def binary_search(movies, movie_id):

    low = 0
    high = len(movies) - 1

    while low <= high:
        mid = (low + high) // 2
        if movies[mid].movie_id == movie_id:
            return movies[mid]
        elif movies[mid].movie_id < movie_id:
            low = mid + 1
        else:
            high = mid - 1

    return None


def display_movie(movie):

    print("-----------------------------")
    print("Movie ID    :", movie.movie_id)
    print("Title       :", movie.title)
    print("Genre       :", movie.genre)
    print("Rating      :", movie.rating)
    print("Watch Count :", movie.watch_count)


def display_all(movies):

    for movie in movies:
        display_movie(movie)


def top_10_movies(movies):

    print("\nTop 10 Highest Rated Movies\n")

    count = 0
    for movie in movies:
        if count == 10:
            break
        display_movie(movie)
        count += 1

def most_watched(movies):

    print("\nMost Watched Movie in Each Genre\n")
    genres = {}
    for movie in movies:
        if movie.genre not in genres:
            genres[movie.genre] = movie
        elif movie.watch_count > genres[movie.genre].watch_count:
            genres[movie.genre] = movie
    for movie in genres.values():
        display_movie(movie)


def main():

    create_database()
    movies = fetch_movies()
    print("\nAll Movies\n")
    display_all(movies)
    sorted_movies = bubble_sort(movies.copy())
    print("\nMovies Sorted by Rating\n")
    display_all(sorted_movies)

    movies_by_id = sorted(movies, key=lambda x: x.movie_id)
    movie_id = int(input("\nEnter Movie ID to Search: "))
    result = binary_search(movies_by_id, movie_id)

    if result:
        print("\nMovie Found\n")
        display_movie(result)
    else:
        print("Movie Not Found")
    top_10_movies(sorted_movies)
    most_watched(movies)


if __name__ == "__main__":
    main()
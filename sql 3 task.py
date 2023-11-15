import sqlite3

con = sqlite3.connect('cinema.db')
cur = con.cursor()
#3
datas = cur.execute("""
SELECT sex,SUM(age)/count() AS average_sex  FROM actors
WHERE sex = 'f'
UNION
SELECT sex,SUM(age)/count() AS average_sex  FROM actors
WHERE sex = 'm'
  """)
for data in datas:
    print(data)

#4
datas = cur.execute("""
SELECT directors.name, directors.surname, MAX(budjet) FROM directors
INNER JOIN movies ON directors.director_id = movies.director_id
""")
for data in datas:
    print(data)

#5
datas = cur.execute("""
SELECT directors.name, directors.surname, COUNT(movies.director_id) AS Kolvo FROM directors
INNER JOIN movies ON directors.director_id = movies.director_id
GROUP BY directors.name
ORDER BY Kolvo DESC
""")
for data in datas:
    print(data)

#6
datas = cur.execute("""
SELECT actors.name, actors.surname, movies.name_movies FROM actors_movies
INNER JOIN movies ON actors_movies.movies_id = movies.movie_id
INNER JOIN actors ON actors_movies.actors_id = actors.actors_id
WHERE movies.budjet>=50000000
""")
for data in datas:
    print(data)

#7
datas = cur.execute("""
SELECT actors.name, actors.surname, COUNT(actors_movies.movies_id) as movie_count
FROM actors
INNER JOIN actors_movies ON actors.actors_id = actors_movies.actors_id
GROUP BY actors.actors_id
ORDER BY movie_count DESC
LIMIT 5;
""")
for data in datas:
    print(data)

#8
datas = cur.execute("""SELECT directors.name, directors.surname, movies.release, COUNT(movies.movie_id) as movie_count
FROM directors 
JOIN movies  ON directors.director_id = movies.director_id
GROUP BY directors.director_id, movies.release
ORDER BY movies.release, movie_count DESC;
""")
for data in datas:
    print(data)


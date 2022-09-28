from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.imdb.com/list/ls055592025/")

imdb_webpage = response.text
soup = BeautifulSoup(imdb_webpage, "html.parser")

movies = soup.find_all(name="h3", class_="lister-item-header")

movie_titles = [movie.getText().replace("\n", "") for movie in movies]

with open("movies.txt", mode="w") as file:
    for n in range(len(movie_titles)):
        file.write(f"{movie_titles[n]}\n")


from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.imdb.com/list/ls055592025/")

imdb_webpage = response.text
soup = BeautifulSoup(imdb_webpage, "html.parser")

movies = soup.find_all(name="a", class_="/title")
print(movies)

movie_list = []
for movie in movies:
    # item = movie.find_all("a")
    items = movie.get_text("href")
    # movie_list.append(item)
    print(items)

# print(movie_list)

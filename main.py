from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.imdb.com/list/ls055592025/")

imdb_webpage = response.text
soup = BeautifulSoup(imdb_webpage, "html.parser")

movies = soup.find_all(name="h3", class_="lister-item-header")
# print(movies)

# movie_list = []
# for movie in movies:
#     item = movie.find_all("a")
#     for i in item:
#         movie_list.append(i)
#     # items = movie.get_text()

movie_titles = [movie.getText() for movie in movies]
print(movie_titles)



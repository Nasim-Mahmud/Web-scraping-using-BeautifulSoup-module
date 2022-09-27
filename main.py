from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2")

empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")

articles = soup.find_all(name="em", class_="jsx")
print(articles)
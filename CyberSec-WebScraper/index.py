import requests
from bs4 import BeautifulSoup

result = requests.get('https://threatpost.com/category/vulnerabilities/')
print(F"Request Code : {result}")
src = result.content
soup = BeautifulSoup(src)

for article in soup.find_all("div", {"class": "o-col-4@md"}):
	h2_tag = article.find("h2", {"class": "c-card__title"})
	print(f"H2 Tag: {h2_tag}")
	a_tag = article.find("p")
	print(f"Summery of article: {a_tag}")
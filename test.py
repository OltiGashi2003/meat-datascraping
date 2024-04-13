import requests
from bs4 import BeautifulSoup

URL = "https://www.ocado.com/browse/fresh-chilled-food-20002/meat-poultry-42114"

titles_list = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all("h4", class_ = "fop-title")
for title in titles:
    title = title.text.strip()
    titles_list.append(title)

print(titles_list)

    
    
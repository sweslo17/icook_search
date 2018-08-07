import requests
import time
import random
import traceback
from tqdm import *
from bs4 import BeautifulSoup

max_page = 100
items = []
for i in tqdm(range(max_page)):
    try:
        param = {
            "ingredients": "",
            "page": i,
            "q": "青椒炒肉絲"
        }
        result = requests.get("https://icook.tw/recipes/search", params=param)
        soup = BeautifulSoup(result.text, "lxml")
        if not soup.find_all("div", class_="browse-recipe-content"):
            break
        for recipe_card in soup.find_all("div", class_="search-browse-recipe"):
            #print(recipe_card)
            card_info = recipe_card.find("div", class_="browse-recipe-content")
            a = card_info.find("a")
            favorite_count = card_info.find("li", class_="browse-recipe-meta-fav").get_text()
            item = {
                "title": a.get_text().strip(),
                "href": "https://icook.tw" + a["href"],
                "favorite_count": int(favorite_count.strip().replace(",", ""))
            }
            items.append(item)
    except:
        print(recipe_card)
        traceback.print_exc()
        break
    time.sleep(random.randint(1,25)/5)
print(sorted(items, key=lambda x:x["favorite_count"], reverse=True))

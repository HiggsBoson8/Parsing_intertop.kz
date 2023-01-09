# Default modules - Модули по умолчанию
import csv
import time
import json
import random
import datetime
from os import system

# Created module - Созданный модуль
from core.config import DOMEN, URL, HEADERS

# Downloaded libraries - Скаченные библиотеки
import requests
from bs4 import BeautifulSoup


# ------------------------------------------------------------------------------------
count_site = int(input("Сколько страниц спарсить: "))
for count  in range(1, count_site + 1):
    responce = requests.get(url=URL, headers=HEADERS, params={"page": f"page-{count}"})
    print(responce.status_code)
    with open(f"core/html/index.html", "a", encoding="UTF-8") as file:
        file.write(responce.text)
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
for count in range(1, count_site + 1):
    with open(f"core/html/index.html", "r") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml").find_all("div", class_="product-item-container")

    with open("core/html/index.html", "w") as file:
        file.write(str(soup))
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
with open("core/html/index.html", "r") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml").find_all("a")
product_info = []

for item in soup:
    url_product = DOMEN + item.get("href")
    name_product = item.get("data-name")
    category_product = item.get("data-category").replace("/", ", ")
    new_prise_product = str(item.find("span", class_="new-product__new-price").text).strip()
    
    information = {
        "url": url_product,
        "name": name_product,
        "category": category_product,
        "new_price": new_prise_product,
    }
    
    product_info.append(information)

with open("core/json/all_product.json", "w", encoding="UTF-8") as file:
    json.dump(product_info, file, indent=4, ensure_ascii=False)
    
    # print("Название:", name_product)
    # print("Ссылка:", url_product)
    # print("Котегория:", category_product)
    # print(f"Цена: {new_prise_product}\n")






    
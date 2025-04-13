import os
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import csv
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GENIMI_API_KEY")

genai.configure(api_key=api_key)


def rewrite_with_gemini(original_text):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(f"Перепиши цей опис промокоду з кращим стилем: {original_text}")
        return response.text.strip()
    except Exception as e:
        print(f"Помилка при зверненні до Gemini API: {e}")
        return "Gemini error"


url = "https://dealspotr.com/promo-codes/search/cat=fashion"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


all_links = soup.find_all("a", class_="gr5")
links = ["https://dealspotr.com" + link["href"] for link in all_links]

current_date = datetime.now().strftime("%Y-%m-%d")

with open("promos_with_urls.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["Store URL", "Promo Code", "Rewritten Description (Genimi)", "Original Description", "Date Found"])

    for link in links:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        all_stores = soup.find_all("span", class_="vam greylinks")
        promos = soup.find_all("div", class_="promoblock--title")

        for store, promo in zip(all_stores,promos):
            promo_text = promo.text.strip()
            store_url = store.find("a")['href']

            original_desc = promo_text
            rewritten_desc = rewrite_with_gemini(original_desc)

            writer.writerow([store_url, promo_text, rewritten_desc, original_desc, current_date])


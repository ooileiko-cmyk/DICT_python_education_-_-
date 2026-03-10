# web_page_scraper.py
import requests
from bs4 import BeautifulSoup
import os
import string
import json

# ===================== Этап 1: Получение цитаты =====================
def get_quote(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Invalid quote resource!")
            return
        data = response.json()
        # Проверяем, есть ли поле 'content'
        if 'content' not in data:
            print("Invalid quote resource!")
            return
        print(data['content'])
    except Exception:
        print("Invalid quote resource!")

# ===================== Этап 2: Парсинг IMDB =====================
def parse_imdb_movie(url):
    try:
        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if response.status_code != 200:
            print("Invalid movie page!")
            return
        soup = BeautifulSoup(response.content, 'html.parser')

        # Получаем заголовок
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else None

        # Получаем описание
        desc_tag = soup.find('meta', {'name': 'description'})
        description = desc_tag['content'].strip() if desc_tag else None

        if not title or not description:
            print("Invalid movie page!")
            return

        # Формируем словарь
        movie_data = {"title": title, "description": description}
        print(movie_data)

    except Exception:
        print("Invalid movie page!")

# ===================== Этап 3: Сохранение исходного кода =====================
def save_page_content(url, filename='source.html'):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"The URL returned {response.status_code}!")
            return
        with open(filename, 'wb') as file:
            file.write(response.content)
        print("Content saved.")
    except Exception as e:
        print(f"Error: {e}")

# ===================== Этап 4: Сохранение статей =====================
def save_articles_from_page(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"The URL returned {response.status_code}!")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        saved_files = []

        for article in articles:
            # Определяем тип статьи
            type_span = article.find('span', {'data-test': 'article.type'})
            article_type = type_span.text.strip() if type_span else None

            if article_type != "News":
                continue  # Берём только новости

            # Ссылка на полную статью
            link_tag = article.find('a', {'data-track-action': 'view article'})
            if not link_tag:
                continue
            article_url = "https://www.nature.com" + link_tag['href']

            # Загружаем статью
            art_response = requests.get(article_url)
            art_soup = BeautifulSoup(art_response.content, 'html.parser')
            body_div = art_soup.find('div', class_=lambda x: x and 'body' in x)
            if not body_div:
                continue
            article_text = body_div.get_text(strip=True)

            # Заголовок статьи
            title_tag = art_soup.find('h1')
            title_text = title_tag.get_text(strip=True) if title_tag else "Article"

            # Формируем имя файла
            filename = title_text.translate(str.maketrans('', '', string.punctuation))
            filename = filename.replace(' ', '_') + '.txt'

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(article_text)
            saved_files.append(filename)

        print(f"Saved articles: {saved_files}")

    except Exception as e:
        print(f"Error: {e}")

        # ===================== Этап 5: Многопостраничный парсинг =====================
        def save_articles_multiple_pages(base_url, pages_count, article_type_filter="News"):
            for page_num in range(1, pages_count + 1):
                page_url = f"{base_url}&page={page_num}"
                folder_name = f"Page_{page_num}"
                os.makedirs(folder_name, exist_ok=True)
                try:
                    response = requests.get(page_url)
                    if response.status_code != 200:
                        print(f"The URL returned {response.status_code} on page {page_num}")
                        continue

                    soup = BeautifulSoup(response.content, 'html.parser')
                    articles = soup.find_all('article')

                    for article in articles:
                        type_span = article.find('span', {'data-test': 'article.type'})
                        art_type = type_span.text.strip() if type_span else None
                        if art_type != article_type_filter:
                            continue

                        link_tag = article.find('a', {'data-track-action': 'view article'})
                        if not link_tag:
                            continue
                        article_url = "https://www.nature.com" + link_tag['href']

                        art_response = requests.get(article_url)
                        art_soup = BeautifulSoup(art_response.content, 'html.parser')
                        body_div = art_soup.find('div', class_=lambda x: x and 'body' in x)
                        if not body_div:
                            continue
                        article_text = body_div.get_text(strip=True)

                        title_tag = art_soup.find('h1')
                        title_text = title_tag.get_text(strip=True) if title_tag else "Article"
                        filename = title_text.translate(str.maketrans('', '', string.punctuation))
                        filename = filename.replace(' ', '_') + '.txt'

                        filepath = os.path.join(folder_name, filename)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(article_text)

                    print(f"Saved all articles from page {page_num}")

                except Exception as e:
                    print(f"Error on page {page_num}: {e}")

        # ===================== Основное меню =====================
        if name == "main":
            print(
                "Выберите этап:\n1 - Цитата\n2 - IMDB\n3 - Сохранение страницы\n4 - Статьи\n5 - Многопостраничные статьи")
            choice = input("> ")

            if choice == "1":
                url = input("Input the URL:\n> ")
                get_quote(url)
            elif choice == "2":
                url = input("Input the URL:\n> ")
                parse_imdb_movie(url)
            elif choice == "3":
                url = input("Input the URL:\n> ")
                save_page_content(url)
            elif choice == "4":
                url = input("Input the URL:\n> ")
                save_articles_from_page(url)
            elif choice == "5":
                base_url = input("Input the base URL (without &page=X):\n> ")
                pages = int(input("Enter number of pages:\n> "))
                article_type = input("Enter article type (default 'News'):\n> ")
                save_articles_multiple_pages(base_url, pages, article_type)
            else:
                print("Invalid choice")
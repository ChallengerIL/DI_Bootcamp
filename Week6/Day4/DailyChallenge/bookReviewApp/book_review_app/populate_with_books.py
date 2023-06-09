import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_review_app.settings")
import django
django.setup()
import requests
from books.models import Book
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
SEARCH_QUERY = 'some query here'

response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={SEARCH_QUERY}')
response_json = response.json()

books = response_json['items']
keys_list = ['title', 'authors', 'publishedDate', 'description', 'pageCount', 'categories', 'imageLinks']

for book in books:
    book = book['volumeInfo']
    if all(key in book for key in keys_list):
        try:
            bool(datetime.strptime(book['publishedDate'], DATE_FORMAT))
        except ValueError:
            pass
        else:
            book_instance = Book(
                title=book['title'],
                author=", ".join(book['authors']),
                published_date=book['publishedDate'],
                description=book['description'],
                page_count=book['pageCount'],
                categories=", ".join(book['categories']),
                thumbnail_url=book['imageLinks']['thumbnail'],
            )
            try:
                book_instance.save()
            except django.db.utils.IntegrityError:
                pass

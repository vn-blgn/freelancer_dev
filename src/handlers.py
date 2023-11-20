import feedparser
from src.id_db import id_db, category_db
from src.urls import urls
from src.helpers import check_entries, make_hashtag, change_pub_date_format, check_category_db


def data_handler():
    tasks = []
    for url in urls:
        data = feedparser.parse(url)
        checked_category_db = check_category_db(data, category_db)
        new_entries = check_entries(data, id_db, 201)
        if checked_category_db and new_entries:
            for element in new_entries:
                category = make_hashtag(element["category"])
                pub_date = change_pub_date_format(element["pub_date"])
                tasks.append(f'<b>{element["title"]}</b> \n'
                             f'\n'
                             f'{element["summary"]} \n'
                             f'\n'
                             f'<a href="{element["link"]}">{pub_date}</a> \n'
                             f'\n'
                             f'{category}')
    return tasks

from datetime import datetime
from src.variables import bot, CHAT_ID


def check_category_db(data, category_db):
    category = data.feed.title
    if category in category_db:
        return 1
    else:
        category_db.append(category)
        return 0


def check_entries(data, links, items):
    new_entries = []
    website = data.feed.link
    if website in links:
        for element in data.entries:
            if element.id not in links[website]:
                new_entries.append({
                    'title': element.title,
                    'link': element.link,
                    'summary': element.summary,
                    'category': element.tags[0].term,
                    'pub_date': element.published
                })
                links[website].append(element.id)
                if len(links[website]) > items:
                    links[website].pop(0)
    return new_entries


async def send_mess(text):
    await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='HTML')


def make_hashtag(category):
    split_category = category.split('/')
    split_category.pop(0)
    new_category = "_".join(split_category).strip().lower().replace(' ', '_').replace('-', '_')
    return f'#{new_category}'


def change_pub_date_format(pub_date):
    datetime_obj = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
    formatted_string = datetime_obj.strftime('%d.%m.%Y, %H:%M')
    return formatted_string

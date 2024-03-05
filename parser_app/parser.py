import requests
from bs4 import BeautifulSoup as BS

URL = 'https://food.ru'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BS(html, "html.parser")
    items = bs.find_all("div",
                        class_="grid_col__GAj_L grid_col_sm_4__K8o8l grid_col_md_8__eM6_K grid_col_lg_6__9iu0E grid_col_offset_md_2__xN8qe")
    food_list = []
    for item in items:
        title_elem = item.find("div", class_="card_title__7LQNy")
        time_elem = item.find("div", class_="card_timeLabel__FjToi card_timeLabelAbsolute__XyPiS")
        image_elem = item.find("div", class_="image_inner__RGeJW")

        if image_elem:
            img_tag = image_elem.find("img")
            if img_tag:
                image = URL + img_tag.get('src')
            else:
                image = None
        else:
            image = None

        if title_elem and time_elem:
            title = title_elem.get_text(strip=True)
            time = time_elem.get_text(strip=True)
            food_list.append({"title": title, "time": time, "image": image})
    return food_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        shoes_list2 = []
        for page in range(1, 10):
            response = get_html('https://food.ru/recipes', params={'page': page})
            shoes_list2.extend(get_data(response.text))
        return shoes_list2
    else:
        raise Exception('Ошибка при парсинге')


# print(parsing())

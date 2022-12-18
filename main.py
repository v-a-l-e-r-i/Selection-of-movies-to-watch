import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

ua = UserAgent()


def crt_dict(film, mark, image):
    sl = {}
    for i in range(len(film)):
        sl = dict(zip(film, zip(mark, image)))

    # for key, value in sorted(sl.items(), key=lambda para: (para[1], para[0]), reverse=True):
    #     if float(value[0]) > 7:
    #         print(f"{key}: {value}")

    with open("file.json", 'w', encoding='utf-8') as file:
        json.dump(sl, file, indent=4, ensure_ascii=False)
        file.close()


def get_info(u, g, f, m, i, inf):
    film = []
    mark = []
    image = []
    page = 1
    while True:
        url = u + str(page) + "/"
        r = requests.get(url, headers={'user-agent': f'{ua.random}'})
        soup = BeautifulSoup(r.content, "lxml")
        gen = soup.find_all(class_=g)
        films = soup.find_all(class_=f)
        marks = soup.find_all(class_=m)
        images = soup.findAll('img', {i: True})

        if len(gen) and page <= 5:
            for item in films:
                film.append(item.text)

            for item in marks:
                mark.append(float(item.text))

            for item in images:
                if str(item[i])[:19] == inf:
                    image.append(f"https://kinoukr.com{str(item[i])}")
            page += 1
        else:
            break

    crt_dict(film, mark, image)







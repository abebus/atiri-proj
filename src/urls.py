"""
Модуль get_urls используется для получения ссылок страниц расположенных
в истории и в закладках браузера.

Note:
    Поддерживаются только следующие браузеры:
        Google Chrome
        YandexBrowser
"""

import os
import sqlite3


def get_urls(browser, mod):
    """
    Вернуть из истории браузера список ссылок и названия сайтов

    :param str browser: название браузера
    :param str mod: откуда брать закладки: History/Bookmarks
    :return: list[tuple], где каждый tuple это (url, title)
    :exception: если браузер не хром и не яндекс, то возвращается строка.
    :exception: если мод указан некорректно (не History и не Bookmarks), то возвращается строка.
    """
    path = os.path.join(r"C:\Users", os.environ.get("USERNAME"), r"AppData\Local")
    if browser == "Chrome":
        path = os.path.join(path, r"Google\Chrome\User Data")
    elif browser == "Yandex":
        path = os.path.join(path, r"Yandex\YandexBrowser\User Data")
    else:
        return "Браузер пока не поддерживается."
    profiles = [
        (
            os.path.join(path, i),
            os.path.getsize(os.path.join(path, i, "History"))
        )
        for i in os.listdir(path) if i == "Default" or i[:7] == "Profile"
    ]
    path = max(profiles, key=lambda x: x[1])[0]
    # max вернет путь к профилю с самой большой историей
    if mod == "History":
        path = os.path.join(path, "History")
        history = sqlite3.connect(path)
        cur = history.cursor()
        cur.execute("SELECT  url, title FROM urls")
        return cur.fetchall()
    if mod == "Bookmarks":
        path = os.path.join(path, "Bookmarks")
        with open(path, "r", encoding="utf-8") as bookmarks:
            urls = []
            for line in bookmarks:
                index = line.find('"url": ')
                if index != -1:
                    urls.append(line[index + 8:-2])
        return urls
    return "Передан неверный режим работы."


if __name__ == "__main__":
    print(get_urls("Chrome", "History"), "\n")
    print(get_urls("Chrome", "Bookmarks"), "\n")
    print(get_urls("Yandex", "History"), "\n")
    print(get_urls("Yandex", "Bookmarks"), "\n")
    print(get_urls("sefe", "Bookmarks"))

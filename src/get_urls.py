"""
Модуль get_urls используется для получения ссылок страниц расположенных
в истории и в закладках браузера.

Note:
    Поддерживаются только слудующие браузеры:
        Google Chrome
        YandexBrowser
"""

import os
import sqlite3


def get_urls_from_history(user, browser, profile="Default"):
    """
    Вернуть из истории браузера список ссылок и названия сайтов

    :param user: имя пользователя пк
    :param browser: название браузера
    :param profile: имя профиля браузера, если профиля нет - Default
    :return: list[tuple], где каждый tuple это (url, title)
    :exception: если браузер не хром и не яндекс, то возвращается строка.
    """
    path = os.path.join(r"C:\Users", user, r"AppData\Local")
    if browser == "Chrome":
        path = os.path.join(path, r"Google\Chrome\User Data")
    elif browser == "Yandex":
        path = os.path.join(path, r"Yandex\YandexBrowser\User Data")
    else:
        return "Браузер пока не поддерживается."
    path = os.path.join(path, profile, "History")
    history = sqlite3.connect(path)
    cur = history.cursor()
    cur.execute("SELECT  url, title FROM urls")
    return cur.fetchall()


def get_url_from_bookmarks(user, browser, profile="Default"):
    """
    Вернуть из закладок браузера список ссылок.

    :param user: имя пользователя пк
    :param browser: название браузера
    :param profile: имя профиля браузера, если профиля нет - Default
    :return: list[str], где каждый элемент это ссылка
    :exception: если браузер не хром и не яндекс, то возвращается строка.
    """
    path = os.path.join(r"C:\Users", user, r"AppData\Local")
    if browser == "Chrome":
        path = os.path.join(path, r"Google\Chrome\User Data")
    elif browser == "Yandex":
        path = os.path.join(path, r"Yandex\YandexBrowser\User Data")
    else:
        return "Браузер пока не поддерживается."
    path = os.path.join(path, profile, "Bookmarks")
    with open(path, "r", encoding="utf-8") as bookmarks:
        urls = []
        for line in bookmarks:
            index = line.find('"url": ')
            if index != -1:
                urls.append(line[index + 8:-2])
    return urls


if __name__ == "__main__":
    print(get_urls_from_history("proil", "Chrome", "Profile 1"), "\n")
    print(get_url_from_bookmarks("proil", "Chrome", "Profile 1"), "\n")
    print(get_urls_from_history("proil", "Yandex"), "\n")
    print(get_url_from_bookmarks("proil", "Yandex"), "\n")
    print(get_url_from_bookmarks("proil", "sefe"))

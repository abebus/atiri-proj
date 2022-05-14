import os
import sqlite3


def get_urls_from_history(user, profile="Default") -> list[tuple]:
    """
    Вернуть из истории браузера список ссылок и названия сайтов

    :param user: имя пользователя пк
    :param profile: имя профиля браузера, если профиля нет - Default
    :return: list[tuple], где каждый tuple это (url, title)
    """
    history = sqlite3.connect(os.path.join(r"C:\Users",
                                           user,
                                           r"AppData\Local\Google\Chrome\User Data",
                                           profile,
                                           "History"))
    cur = history.cursor()
    cur.execute("SELECT  url, title FROM urls")
    return cur.fetchall()


def get_url_from_bookmarks(user, profile="Default") -> list[str]:
    """
    Вернуть из закладок браузера список ссылок.

    :param user: имя пользователя пк
    :param profile: имя профиля браузера, если профиля нет - Default
    :return: list[str], где каждый элемент это ссылка
    """
    with open(os.path.join(r"C:\Users",
                           user,
                           r"AppData\Local\Google\Chrome\User Data",
                           profile,
                           "Bookmarks"),
              "r", encoding="utf-8") as bookmarks:
        urls = []
        for line in bookmarks:
            index = line.find('"url": ')
            if index != -1:
                urls.append(line[index + 8:-2])
    return urls

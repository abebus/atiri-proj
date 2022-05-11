import sqlite3


def get_urls(user, profile="Default") -> list[tuple]:
    """
    Вернуть из истории браузера список ссылок и названия сайтов

    :param user: имя пользователя пк
    :param profile: имя профиля браузера, если профиля нет - Default
    :return: list[tuple], где каждый tuple это (url, title)
    """
    history = sqlite3.connect(f"C:\\Users\\{user}\\AppData\\Local\\"
                              f"Google\\Chrome\\User Data\\{profile}\\History")
    cur = history.cursor()
    cur.execute("SELECT  url, title FROM urls")
    return cur.fetchall()


if __name__ == "__main__":
    print(get_urls("proil", "Profile 1"))

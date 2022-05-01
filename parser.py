import os
import uuid
import re
import requests as req
import bs4 as bs
from src.maps.hash_map import HashMap


def wiki_parser(url: str, base_path: str):
    """
    :param str url: адрес страницы вики.
    :param str base_path: путь к папке, в которой создастся папка base_path. Это родительская
        папка, в которой будут храниться папки с результатами.
    """
    # Создание родительской папки.
    base_path += "\\base_path"
    try:
        os.mkdir(base_path)
    except OSError:
        print("Создание не удалось: папка base_path уже создана.")
    else:
        print("Папка base_path создана.")
    # Проверка на наличия url в сохраненных файлах.
    flag = True
    dirlist = os.listdir(base_path)
    path = base_path  # путь до папки с файлами url.txt и content.bin
    for i in dirlist:
        with open(base_path + "\\" + i + "\\url.txt", "r", encoding="utf-8") as url_file:
            if url_file.read() == url:
                flag = False
                path += "\\" + i
                break
    # Если url не нашелся, то создать папку с файлами url.txt, content.bin
    if flag:
        path += "\\" + uuid.uuid4().hex
        os.mkdir(path)
        text = req.request("GET", url).content
        with open(path + "\\content.bin", "wb") as content_file:
            content_file.write(text)
        with open(path + "\\url.txt", "w", encoding="utf-8") as url_file:
            url_file.write(url)
    # Подсчет слов с помощью HashMap. Сериализация HashMap в файл words.txt
    with open(path + "\\text.txt", "w", encoding="utf-8") as file:
        with open(path + "\\content.bin", "rb") as content_file:
            soup = bs.BeautifulSoup(content_file, "lxml")
            dict_of_words = {}
            for string in soup.stripped_strings:
                string = string.replace(".", "")
                string = string.replace(":", "")
                string = string.replace(";", "")
                string = string.replace(",", "")
                string = string.replace("«", "")
                string = string.replace("»", "")
                for word in string.split():
                    if word[0] in r"""<>¶—`~1234567890!@#$%^&*()-=_+[]{}\|/,.?'"№:;""":
                        continue
                    file.write(word+" ")

if __name__ == "__main__":
    wiki_parser('https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html',
                r'D:\For_Python\Informatics_two_term_Kharin_Ildar\src')

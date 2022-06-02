from urls import *
from parser1 import *
from tf_idf import *
from sqllite3_atiri import *
from project import *


choose = {
        'IT'        : r'https://www.it-world.ru/',
        'python'    : r'https://python.org/',
        'cpp'       : r'https://itproger.com/course/cpp',
        'java'      : r'https://habr.com/ru/search/?q=java&target_type=posts&order=relevance',
        'sport'     : r'http://ru.sport-wiki.org/',
        'health'    : r'https://apteka.ru/',
        'literature': r'http://parnasse.ru/'
         }

choose1 = dict()
with open('dict.TXT') as dictt:
    for row in dictt:
        ro1 = row.strip().split()
        if ro1:
            theme, selected = row.strip().split()
            choose1.update({theme: selected})


    def bebus(them):
        answer = []
        standart = parser(choose[them])
        for i in f:
            if comparison(standart, i[0]) >= 0.05:
                answer.append((i[0],))
                # print(i[0])
        return answer, them


if __name__ == '__main__':
    f = get_urls('Chrome', 'Bookmarks')
    for themee in choose:
        insert_multiple_records(*bebus(themee))
    start()

    # wtf
    # print(parser(i[0]))

    # print(get_urls_from_history('Professional', 'Chrome', 'Profile 1'))

from urls import *
from parser1 import *
from tf_idf import *
from sqllite3_atiri import *
from project import *

def final():
    answer = []
    f = get_urls('Chrome', 'History')
    #parser('https://python.org', 'both')
    standart = parser('https://www.youtube.com')
    for i in f:
        if comparison(standart, i[0]) >= 0.05:
            answer.append((i[0],))
            #print(i[0])
    return answer

if __name__ == '__main__':
    insert_multiple_records(final())
    start()

    #wtf
        #print(parser(i[0]))

    #print(get_urls_from_history('Professional', 'Chrome', 'Profile 1'))

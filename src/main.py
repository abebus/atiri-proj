from urls import *
from parser1 import *
from tf_idf import *
from sqllite3_atiri import *

def final():
    answer = []
    f = get_urls_from_history('Professional', 'Chrome', 'Profile 1')
    #parser('https://python.org', 'both')
    standart = parser('https://python.org')
    for i in f:
        if comparison(standart, i[0]) >= 0.05:
            answer.append((i[0],))
            #print(i[0])
    return answer

if __name__ == '__main__':
    insert_multiple_records(final())

    #wtf
        #print(parser(i[0]))

    #print(get_urls_from_history('Professional', 'Chrome', 'Profile 1'))

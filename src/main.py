from get_urls import *
from new_parser import *
from tf_idf import *



if __name__ == '__main__':
    f = get_urls_from_history('Professional', 'Chrome', 'Profile 1')
    #parser('https://python.org', 'both')
    standart = parser('https://python.org')
    for i in f:
        if comparison(standart, i[0]) >= 0.05:
            print(i[0])
        #print(parser(i[0]))

    #print(get_urls_from_history('Professional', 'Chrome', 'Profile 1'))

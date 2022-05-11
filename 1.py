import collections
import math


def splittolist(page):
    f = open(page, encoding = 'utf-8')
    splitted = []
    for line in f:
        splitted.append(line.split())
    f.close()
    return splitted

def flat(list_):
    flat = []
    for sublist in list_:
        for elem in sublist:
            flat.append(elem)
    return flat

def computetf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

def computeidf(word, corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

def computetf_idf(list_):
    '''Принимает список из плоских списков'''
    documents_list = []
    for text in list_:
        tf_idf_dictionary = {}
        computed_tf = computetf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * computeidf(word, list_)
        documents_list.append(tf_idf_dictionary)
    return (documents_list)


if __name__ == '__main__':
    #print(splittolist('page1.txt'))
    wordlist1 = splittolist('test1.txt')
    flat_wordlist1 = flat(wordlist1)
    wordlist2 = splittolist('test2.txt')
    flat_wordlist2 = flat(wordlist2)
    wordlist3 = splittolist('test3.txt')
    flat_wordlist3 = flat(wordlist3)

    mainlist = [flat_wordlist1, flat_wordlist2, flat_wordlist3]
    #print(flat_wordlist3)

    #print(computetf(flat_wordlist1))
    #print(computetf(flat_wordlist2))
    print(computetf_idf(mainlist)[0])
    

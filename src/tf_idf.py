from sklearn.feature_extraction.text import TfidfVectorizer

def comparison(text1, text2):
    #with open('file1.txt', 'r', encoding = 'utf-8') as F:
        #file1 = F.read()
    #with open('file2.txt', 'r', encoding = 'utf-8') as F:
        #file2 = F.read()

    tfidf = TfidfVectorizer()
    vecs = tfidf.fit_transform([text1, text2])
    corr_matrix = ((vecs * vecs.T).A)
    similarity = corr_matrix[0,1]
    return similarity


if __name__ == '__main__':
    comparison()

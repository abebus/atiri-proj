from sklearn.feature_extraction.text import TfidfVectorizer


with open('file1', 'r', encoding = 'utf-8') as F:
    file1 = F.read()

with open('file2', 'r', encoding = 'utf-8') as F:
    file2 = F.read()

tfidf = TfidfVectorizer()
vecs = tfidf.fit_transform([file1, file2])
corr_matrix = ((vecs * vecs.T).A)
similarity = corr_matrix[0,1]
print(similarity)

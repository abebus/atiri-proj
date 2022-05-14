from sklearn.feature_extraction.text import TfidfVectorizer


with open('file1', 'r', encoding = 'utf-8') as F:
    inception = F.read()

with open('file2', 'r', encoding = 'utf-8') as F:
    shutter_island = F.read()

tfidf = TfidfVectorizer()
vecs = tfidf.fit_transform([inception, shutter_island])
corr_matrix = ((vecs * vecs.T).A)
similarity = corr_matrix[0,1]
print(similarity)

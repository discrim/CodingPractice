import nltk
import random
from nltk.corpus import movie_reviews
 
# https://www.pythonprogramming.net/text-classification-nltk-tutorial/
 
# =======================================
# -- Corpus of movie_reviews
# =======================================
 
print("category: ", movie_reviews.categories())
 
# -- review filename
print("pos files: ", movie_reviews.fileids('pos')[:5])   # positive
print("neg files: ", movie_reviews.fileids('neg')[:5])   # negative
print("... movie_reviews.fileids", "." * 100, "\n")
 
# -- review words
print("pos words sample: ", list(movie_reviews.words('pos/cv645_15668.txt'))[:10])
print("neg words sample: ", list(movie_reviews.words('neg/cv999_14636.txt'))[:10])
print("... movie_reviews.words", "." * 100, "\n")
 
# -- collect reviews.words
# documents = ([word1, wor2, ...wordx], 'pos')
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
 
print(documents[1])
print("... all_documents", "." * 100, "\n")
 
# -- random.shuffle
random.shuffle(documents)
 
print(documents[1])
print("... shuffled_all_documents", "." * 100, "\n")
 
 
# =======================================
# -- Get word & frequency
# =======================================
all_words = []
 
# -- 소문자 변환
for w in movie_reviews.words():
    all_words.append(w.lower())
 
# -- get word frequency / word count vector
all_words = nltk.FreqDist(all_words)
 
# -- output top 15
print(all_words.most_common(15))
 
seq = 1
for word, frequency in all_words.most_common(15):
    print("[",seq ,"] *word:",word, " *cnt:",frequency)
    seq += 1
 
print(",,, output_top_15_words", "," * 100, "\n")
 
# -- extract words only
print(list(all_words.keys())[:50])
print(",,, extract_words_only", "," * 100, "\n")
 
# -- frequency word count
print("freq_word count :", len(all_words))
print(",,, freq_word_count", "," * 100, "\n")
 
# -- get word frequency
print(all_words["and"])
print(",,, get_word_frequency", "," * 100, "\n")
 
 
# =======================================
# -- Word Features
# =======================================
word_features = list(all_words.keys())[:3000] # 개수가 작으면 accuracy가 낮아짐
 
print(word_features)
print(";;; word_features", ";" * 100, "\n")
 
# -- find_features 함수
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
 
    return features
 
featuresets = [(find_features(words), category) for (words, category) in documents]
 
print(featuresets[:1])
print(";;; features sets", ";" * 100, "\n")
 
 
# =======================================
# -- Write list to dmp
# =======================================
 
# Ref : dbrang.tistory.com/1240
import pickle
 
with open('featuresets.dmp', 'wb') as fp:
    pickle.dump(featuresets, fp)
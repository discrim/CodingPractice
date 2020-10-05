import nltk
from nltk.tokenize import word_tokenize as wt

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ('What an awesome view', 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'), 
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')    
]

all_words = sorted(set(word.lower() for passage in train for word in wt(passage[0])))
print(all_words)

aw2 = nltk.FreqDist(all_words)
print(aw2.most_common(5))

features = [({word: (word in wt(xx[0])) for word in all_words}, xx[1]) for xx in train]
for elem in features:
    print(elem)

nbc = nltk.NaiveBayesClassifier.train(features)
nbc.show_most_informative_features()

test = "This is the best band I've ever heard!"
test_features = {word: (word.lower() in wt(test.lower())) for word in all_words}
print(test_features)

print(nbc.classify(test_features))
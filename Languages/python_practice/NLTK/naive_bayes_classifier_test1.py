import nltk
from nltk.tokenize import word_tokenize as wt

train = [
    ('I like you', 'pos'),
    ('I hate you', 'neg'),
    ('you like me', 'neg'),
    ('I like her', 'pos')
]

all_words = sorted(set(word.lower() for passage in train for word in wt(passage[0])))
print(all_words)

t_bin = [
        ({word: (word in wt(xx[0])) for word in all_words}, xx[1]) for xx in train
]

for ea in t_bin:
    print(ea)

classifier = nltk.NaiveBayesClassifier.train(t_bin)
classifier.show_most_informative_features()

test = "I like table"
test_feature = {word: (word in wt(test.lower())) for word in all_words}
print(test_feature)
print(classifier.classify(test_feature))
import nltk
from nltk.tokenize import word_tokenize as wt

def countFromList(st, lst):
    histo = dict()
    for key in st:
        histo[key] = 0
    for ii in range(len(lst)):
        histo[lst[ii]] += 1
    return histo

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

features = []
for passage in train:
    tmpdict = {}
    for word in all_words:
        tmpdict[word] = passage[0].count(word)
        #tmpdict[word] = word in wt(passage[0])
    features.append((tmpdict, passage[1]))
for elem in features:
    print(elem)

nbc = nltk.NaiveBayesClassifier.train(features)
nbc.show_most_informative_features()

test = "This is the best band I've ever heard!"
#test_features = {word: (word.lower() in wt(test.lower())) for word in all_words}
test_features = {word: wt(test.lower()).count(word) for word in all_words}
print(test_features)

print(nbc.classify(test_features))
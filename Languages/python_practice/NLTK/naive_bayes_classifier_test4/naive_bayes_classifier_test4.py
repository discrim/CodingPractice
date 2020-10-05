import nltk
from nltk.tokenize import word_tokenize as wt


# Description: Trains the naive Bayes classifier.
# Inputs: String for the file location of the training data (the "training" directory).
# Outputs: An object representing the trained model.
def train(training_path):
    # TODO: implement data loading, preprocessing, and model training
    
    # Load
    from os import listdir
    vocab = set([])
    pospath = training_path + r"\pos"
    negpath = training_path + r"\neg"
    posfiles = listdir(pospath)
    negfiles = listdir(negpath)
    
    for fn in posfiles:
        ff = open(pospath + '/' + fn)
        fstr = ff.read()
        tokens = [word.lower() for word in wt(fstr)]
        vocab.update(tokens)
    
    for fn in negfiles:
        ff = open(negpath + '/' + fn)
        fstr = ff.read()
        tokens = [word.lower() for word in wt(fstr)]
        vocab.update(tokens)
    
    vocab = sorted(vocab)
    
    # Preprocess
    features = []
    for fn in posfiles:
        ff = open(pospath + '/' + fn)
        fstr = ff.read()
        tmpdict = {}
        for word in vocab:
            tmpdict[word] = wt(fstr).count(word)
        features.append((tmpdict, 'pos'))
    for fn in negfiles:
        ff = open(negpath + '/' + fn)
        fstr = ff.read()
        tmpdict = {}
        for word in vocab:
            tmpdict[word] = wt(fstr).count(word)
        features.append((tmpdict, 'neg'))
    
    # Train
    trained_model = nltk.NaiveBayesClassifier.train(features)
    
    return trained_model


# Description: Runs prediction of the trained naive Bayes classifier on the test set, and returns these predictions.
# Inputs: An object representing the trained model (whatever is returned by the above function), and a string for the file location of the test data (the "testing" directory).
# Outputs: An object representing the predictions of the trained model on the testing data, and an object representing the ground truth labels of the testing data.
def predict(trained_model, testing_path):
    # TODO: implement data loading, preprocessing, and model prediction
    from os import listdir
    pospath = testing_path + r"/pos"
    negpath = testing_path + r"/neg"
    posfiles = listdir(pospath)
    negfiles = listdir(negpath)
    
    # Preprocess
    features_and_gt = []
    for fn in posfiles:
        ff = open(pospath + '/' + fn)
        flst = wt(ff.read())
        fset = set(flst)
        tmpdict = {}
        for key in fset:
            tmpdict[key] = flst.count(key)
        #for word in vocab:
        #    tmpdict[word] = word in wt(fstr)
        features_and_gt.append((tmpdict, 'pos'))
    for fn in negfiles:
        ff = open(negpath + '/' + fn)
        flst = wt(ff.read())
        fset = set(flst)
        tmpdict = {}
        for key in fset:
            tmpdict[key] = flst.count(key)
        #for word in vocab:
        #    tmpdict[word] = word in wt(fstr)
        features_and_gt.append((tmpdict, 'neg'))
    print(features_and_gt[0])
    
    # Predict
    model_predictions = []
    ground_truth = []
    for elem in features_and_gt:
        print("body: ", elem[0])
        print("senti: ", elem[1])
        model_predictions.append(trained_model.classify(elem[0]))
        ground_truth.append(elem[1])
    
    return model_predictions, ground_truth


# Description: Evaluates the accuracy of model predictions using the ground truth labels.
# Inputs: An object representing the predictions of the trained model, and an object representing the ground truth labels for the testing data.
# Outputs: Floating-point accuracy of the trained model on the test set.
def evaluate(model_predictions, ground_truth):
    # TODO: implement evaluation metrics for the predictions
    right_count = 0
    wrong_count = 0
    for ii in range(len(model_predictions)):
        if model_predictions[ii] == ground_truth[ii]:
            right_count += 1
        else:
            wrong_count += 1
    accuracy = right_count / (right_count + wrong_count)
    return accuracy


if __name__ == '__main__':
    TRAINING_PATH = r"D:\Desktop\code_practice\python_practice\NLTK\naive_bayes_classifier_test4\train_data"
    TESTING_PATH = r"D:\Desktop\code_practice\python_practice\NLTK\naive_bayes_classifier_test4\test_data"
    trained_model = train(TRAINING_PATH)
    trained_model.show_most_informative_features()
    model_predictions, ground_truth = predict(trained_model, TESTING_PATH)
    accuracy = evaluate(model_predictions, ground_truth)
    print('Accuracy: %s' % str(accuracy))
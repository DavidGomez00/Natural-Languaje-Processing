import nltk
from nltk.corpus import names
import random


def gender_features(word):
    '''Return the important features about the name gender.'''
    return {'sufix1': word[-1],         # last letter of the name
            'suffix2': word[-2:],       # last two letthers of the name
            'prefix1': word[3:],        # first three letters of the name
            'length' : len(word)}       # length of the name

def main():
    # Get all names in the corpus
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] 
                + [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(labeled_names)

    # Get a set with labeled names
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
    # Divide the set in the training and test set
    # 0 - 500 for the test set
    test_set = featuresets[0:500]
    # 500 - 1000 for the dev-test set
    devtest_set = featuresets[500:1000]
    # The remaining for the training set
    train_set = featuresets[1000:]


    # Create a classifier with the Naive Bayes Model
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    # Print the accuracy on dev_test        
    # print(f'Accuracy with dev_test: {nltk.classify.accuracy(classifier, devtest_set)}')

    # Finally print the accuracy on the test_set
    print(f'Accuracy with final test: {nltk.classify.accuracy(classifier, test_set)}')

if __name__ == "__main__":
    main()
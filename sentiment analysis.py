import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names


class Sentiment:
    def word_feats(self, words):
        return dict([(word, True) for word in words])

    positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
    negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(', 'not', 'tired']
    neutral_vocab = ['car', 'the', 'sound', 'was', 'is', 'price', 'did', 'know', 'words', 'not', 'okay']

    positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
    negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
    neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

    train_set = negative_features + positive_features + neutral_features

    classifier = NaiveBayesClassifier.train(train_set)

    # Predict
    neg = 0
    pos = 0
    sentence = "not too good or bad"
    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in words:
        classResult = classifier.classify(word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1

    print('Positive: ' + str(float(pos) / len(words)))
    print('Negative: ' + str(float(neg) / len(words)))

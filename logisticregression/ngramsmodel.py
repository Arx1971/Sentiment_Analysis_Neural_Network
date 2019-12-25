import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import math


# nltk.download('stopwords') download all the stopwords

def dictionary_frequency_viewer(dictionary):
    for key, values in dictionary.items():
        print(key, values)


def regression(reviews, dictionary, tdf_dictionary):
    with open(reviews, 'r') as lines:
        for line in lines:
            documents_frequency = dict()
            words = line.split()
            for word in words:
                if word in documents_frequency:
                    documents_frequency[word] += 1
                else:
                    documents_frequency[word] = 1
            mle = 0.0
            for word in words:
                idf = math.log(2, (1 + 12500) / 1 + tdf_dictionary.get(word, 0)) + 1
                tf = documents_frequency[word]
                tf_idf = tf * idf


def bag_of_word_model(reviews):
    dictionary = dict()
    idf_dictionary = dict()
    frequency = dict()
    stop_words = set(stopwords.words('english'))
    with open(reviews, 'r') as lines:
        for line in lines:
            words = line.split()
            for word in words:
                frequency[word] = 1
                if word not in stop_words:
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
            for key, values in frequency.items():
                if key in idf_dictionary:
                    idf_dictionary[key] += 1
                else:
                    idf_dictionary[key] = 1

    return dictionary, idf_dictionary


positive = bag_of_word_model('positive_reviews_train.txt')
positive_vocabulary = positive[0]
positive_idf = positive[1]
negative = bag_of_word_model('negative_reviews_train.txt')
negative_vocabulary = negative[0]
negative_idf = negative[1]

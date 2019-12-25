import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import math
from logisticregression.activationvalues import sigmoid_function
from collections import Counter


# nltk.download('stopwords') download all the stopwords

def dictionary_frequency_viewer(dictionary):
    for key, values in dictionary.items():
        print(key, values)


def merge_vocabulary(vocabulary_1, vocabulary_2):
    x = Counter(vocabulary_1)
    y = Counter(vocabulary_2)
    x.update(y)
    return dict(x)


def sum_of_values(dictionary):
    total = 0
    for key, values in dictionary.items():
        total += values
    return total


def regression(reviews, dictionary, tdf_dictionary, total_word_in_class, total_vocabulary_size):
    positive_counter = 0
    negative_counter = 0
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
                idf = float(math.log((1 + 12500) / 1 + tdf_dictionary.get(word, 0)) + 1)
                tf = documents_frequency[word]
                tf_idf = float(tf * idf)
                prob = float((dictionary.get(word, 0) + 1) / (total_word_in_class + total_vocabulary_size))
                mle += math.log(prob * tf_idf)

            value = sigmoid_function(mle)
            print(value)
            if value >= 0.5:
                positive_counter += 1
            else:
                negative_counter += 1

    return positive_counter, negative_counter


def bag_of_word_model(reviews):
    dictionary = dict()
    idf_dictionary = dict()
    frequency = dict()
    total_number_word_in_class = 0
    stop_words = set(stopwords.words('english'))
    with open(reviews, 'r') as lines:
        for line in lines:
            words = line.split()
            for word in words:
                total_number_word_in_class += 1
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

    return dictionary, idf_dictionary, total_number_word_in_class


positive = bag_of_word_model('positive_reviews_train.txt')
positive_vocabulary = positive[0]
positive_idf = positive[1]
total_positive_word = positive[2]
negative = bag_of_word_model('negative_reviews_train.txt')
negative_vocabulary = negative[0]
negative_idf = negative[1]
total_negative_word = negative[2]
total_vocabulary = merge_vocabulary(negative_vocabulary, positive_vocabulary)
total_size = len(total_vocabulary)
print(regression('positive_reviews_test.txt', positive_vocabulary, positive_idf, total_positive_word, total_size))

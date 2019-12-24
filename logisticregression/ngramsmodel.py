import re
from string import punctuation


def dictionary_frequency_viewer(dictionary):
    for values, key in dictionary.items():
        print(values, key)


def bag_of_word_model(reviews):
    dictionary = dict()
    with open(reviews, 'r') as lines:
        for line in lines:
            words = line.split()
            for word in words:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return dictionary


positive_vocabulary = bag_of_word_model('positive_reviews.txt')
negative_vocabulary = bag_of_word_model('negative_reviews.txt')

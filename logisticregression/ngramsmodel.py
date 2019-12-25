import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


# nltk.download('stopwords') download all the stopwords

def dictionary_frequency_viewer(dictionary):
    for values, key in dictionary.items():
        print(values, key)


def bag_of_word_model(reviews):
    dictionary = dict()
    idf_dictionary = dict()
    frequency = set()
    stop_words = set(stopwords.words('english'))
    with open(reviews, 'r') as lines:
        for line in lines:
            words = line.split()
            for word in words:
                frequency.add(word)
                if word not in stop_words:
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
            for word in frequency:
                if word in idf_dictionary:
                    idf_dictionary[word] += 1
                else:
                    idf_dictionary[word] = 1
    return dictionary, idf_dictionary


positive_vocabulary = bag_of_word_model('positive_reviews_train.txt')[0]
negative_vocabulary = bag_of_word_model('negative_reviews_train.txt')[0]
dictionary_frequency_viewer(negative_vocabulary)

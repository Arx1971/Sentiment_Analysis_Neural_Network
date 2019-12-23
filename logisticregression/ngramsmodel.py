import re
from string import punctuation


def dictionary_frequency_viewer(dictionary):
    for values, key in dictionary.items():
        print(values, key)


def bag_of_word_model(filename, filepath):
    dictionary = dict()
    for file in filename:
        with open(filepath + file, "r") as reviews:
            review = reviews.read()
            review = re.sub(r'[`=~!@#$%^&*()_+\[\]{};\\:"|<,./<>?^]', ' ', review)
            words = review.split()
            for word in words:
                word = word.lower()
                word = word.strip(punctuation)
                word = word.strip()
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    return dictionary

import re
from string import punctuation
from logisticregression.filereader import read_all_file_name


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


def write_file(filepath, review, filename):
    file = open(filename, 'w+')
    for review_name in review:
        with open(filepath + review_name, "r") as reviews:
            review = reviews.read()
            review = re.sub(r'[`=~!@#$%^&*()_+\[\]{};\\:"|<,./<>?^]', ' ', review)
            words = review.split()
            for word in words:
                word = word.lower()
                word = word.strip(punctuation)
                word = word.strip()
                file.write(word + " ")
    file.close()


# path = "/home/adnan/source-code/PycharmProjects/Sentiment_Classification_Logistic_Regeression/aclImdb/train/"
# positive_review_name = read_all_file_name(path + "pos")
# negative_review_name = read_all_file_name(path + "neg")
# pos_dictionary = bag_of_word_model(positive_review_name, path + "pos/")
# neg_dictionary = bag_of_word_model(negative_review_name, path + "neg/")
# dictionary_frequency_viewer(neg_dictionary)

import re
from string import punctuation
from logisticregression.filereader import read_all_file_name


def write_on_file(filenames, doc_name, filepath):
    doc = open(doc_name, 'w+')
    for file in filenames:
        with open(filepath + file, 'r') as reviews:
            review = reviews.read()
            review = re.sub(r'[`=~!@#$%^&*()_+\[\]{};\\:"|<,./<>?^]', ' ', review)
            words = review.split()
            doc.write('<s> ')
            for word in words:
                word = word.lower()
                word = word.strip(punctuation)
                word = word.strip()
                doc.write(word + " ")
            doc.write('</s>\n')
    doc.close()


path = "/home/adnan/source-code/PycharmProjects/Sentiment_Classification_Logistic_Regeression/aclImdb/train/"
positive_review_name = read_all_file_name(path + 'pos')
write_on_file(positive_review_name, 'positive_reviews.txt', path + 'pos/')
negative_review_name = read_all_file_name(path + 'neg')
write_on_file(negative_review_name, 'negative_reviews.txt', path + 'neg/')

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


path = "/home/adnan/source-code/PycharmProjects/Sentiment_Classification_Logistic_Regeression/aclImdb/"
train_positive_review_name = read_all_file_name(path + 'train/pos')
write_on_file(train_positive_review_name, 'positive_reviews_train.txt', path + 'train/pos/')
train_negative_review_name = read_all_file_name(path + 'train/neg')
write_on_file(train_negative_review_name, 'negative_reviews_train.txt', path + 'train/neg/')
test_positive_review_name = read_all_file_name(path + 'test/pos')
write_on_file(test_positive_review_name, 'positive_reviews_test.txt', path + 'test/pos/')
test_negative_review_name = read_all_file_name(path + '/test/neg')
write_on_file(test_negative_review_name, 'negative_reviews_test.txt', path + 'test/neg/')

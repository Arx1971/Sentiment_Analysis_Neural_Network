import os
import re
from string import punctuation
from logisticregression.filereader import read_all_file_name


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

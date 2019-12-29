import pandas as pd
import numpy as np
import io
import os


def load_data_set(review_path, label):
    res = []
    with open(review_path, 'r') as lines:
        for line in lines:
            res.append([line, label])

    return res


positive_review_path = '../pre_process/negative_reviews_train.txt'
negative_review_path = '../pre_process/negative_reviews_train.txt'

pos_data_set = load_data_set(positive_review_path, 1)
neg_data_set = load_data_set(negative_review_path, 0)
pos_data_set.extend(neg_data_set)

df = pd.DataFrame(pos_data_set, columns=['Review', 'Label'])
np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))
df.to_csv('./movie_review.csv', index=False, encoding='utf-8')


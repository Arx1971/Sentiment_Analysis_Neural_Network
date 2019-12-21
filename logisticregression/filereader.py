import os


def read_all_file_name(filepath):
    files = []
    for i in os.listdir(filepath):
        if i.endswith(".txt"):
            files.append(i)
    return files


def main():
    file_path_train = "/home/adnan/source-code/PycharmProjects/Sentiment_Classification_Logistic_Regeression/aclImdb" \
                      "/train"
    file_path_test = "/home/adnan/source-code/PycharmProjects/Sentiment_Classification_Logistic_Regeression/aclImdb" \
                     "/test"
    train_pos_file_names = read_all_file_name(file_path_train + "/pos")

    print(train_pos_file_names)


if __name__ == '__main__':
    main()

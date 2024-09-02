import json
import random
import csv

import re

# def separate_periods(sentence):
#     # 使用正则表达式匹配不需要分开的情况
#     pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)'
#     separated_sentence = re.sub(pattern, '@@@@@@@@@', sentence)
#     return separated_sentence

def convert_to_sequence_labeling(csv_file_path, txt_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file, open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        data = csv.reader(csv_file)
        # print("data:", data)
        # 跳过第一行（标题行）
        next(data)
        for row in data:
            print(row[1])
            title = row[1]
            decisions = row[2]
            title = title.replace(',', ' ,')
            title = title.replace(':', ' :')
            title = title.replace(';', ' ;')
            title = title.replace('\'', ' \'')
            title = title.replace('?', ' ?')
            #
            # print("title:", title)
            # print("decisions:", decisions)

            # 初始化标签列表，所有单词的标签默认为 'O'
            labels = ['O'] * len(title.split())

            # 使用 eval() 函数解析 Decisions 字段中的字典
            decisions_dict = eval(decisions)
            # 获取字典中的每一个键值对
            items = decisions_dict.items()

            # 遍历每一个键值对并输出
            for entity, label in items:
                print(f"实体: {entity}, 标签: {label}")
                # 将标签更新到标签列表中
                words = title.split()
                # print(words, "\n")

                for i in range(len(words)):
                    if words[i] in entity:
                        if label == 'positive':
                            labels[i] = 'T-POS'
                        elif label == 'negative':
                            labels[i] = 'T-NEG'
                        elif label == 'neutral':
                            labels[i] = 'T-NEU'
            # 将句子和标签写入文件
            content = title.lstrip().rstrip()  #去掉句子前面和后面多余的空格
            txt_file.write(f"{content}####")
            for word, label in zip(content.split(), labels):
                txt_file.write(f"{word}={label} ")

            # 写入换行符
            txt_file.write('\n')

def split_data(input_file, train_file, dev_file, test_file, train_ratio=0.7, dev_ratio=0.1, test_ratio=0.2):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.readlines()

    total_size = len(data)
    train_size = int(total_size * train_ratio)
    dev_size = int(total_size * dev_ratio)
    test_size = total_size - train_size - dev_size

    # 随机打乱数据
    random.shuffle(data)

    # 分割数据
    train_data = data[:train_size]
    dev_data = data[train_size:train_size + dev_size]
    test_data = data[train_size + dev_size:]

    # 写入分割后的数据到相应文件
    with open(train_file, 'w', encoding='utf-8') as file:
        file.writelines(train_data)

    with open(dev_file, 'w', encoding='utf-8') as file:
        file.writelines(dev_data)

    with open(test_file, 'w', encoding='utf-8') as file:
        file.writelines(test_data)


if __name__ == "__main__":
    csv_file_path = "financialNews.csv"
    txt_file_path = "SEntFiN.txt"

    convert_to_sequence_labeling(csv_file_path, txt_file_path)
    print("数据转换完成。")

# 使用示例
    split_data(txt_file_path, 'fin_train.txt', 'fin_dev.txt', 'fin_test.txt')
    print("数据分割完成。")

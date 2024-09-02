import json
import random
import csv
import os

import re


def transform_dict_to_list(input_dict):
    input_dict = json.loads(input_dict)
    output_list = []
    for key, value in input_dict.items():
        new_dict = {"value": key, "tag": value}
        output_list.append(new_dict)

    return output_list

def convert_to_llama(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        data = csv.reader(csv_file)
        # print("data:", data)
        # 跳过第一行（标题行）
        next(data)
        news = []
        for row in data:
            new = {}
            # print(row[1])
            title = row[1]
            decisions = row[2]
            # title = title.replace(',', ' ,')
            # title = title.replace(':', ' :')
            # title = title.replace(';', ' ;')
            # title = title.replace('\'', ' \'')
            # title = title.replace('?', ' ?')
            #
            # print("title:", title)
            # print("decisions:", decisions)
            new_aanos = transform_dict_to_list(decisions)
            # print(new_aanos)
            if len(new_aanos)==1:
                output = json.dumps(new_aanos[0])

            else:
                output = json.dumps(new_aanos[0])
                for new_anno in new_aanos[1:]:
                    output = output+"\n"+ json.dumps(new_anno)

            new["id"] = row[0]
            new["content"] = title
            new["input"] = ""
            new["output"] = output

            news.append(new)
        return news

def split_data(seed, news, data_file_path, train_ratio=0.8):

    data = news

    total_size = len(data)
    train_size = int(total_size * train_ratio)

    # 随机打乱数据
    random.seed(seed)
    random.shuffle(data)

    # 分割数据
    train_data = data[:train_size]
    test_data = data[train_size:]

    for item in train_data:
        item["instruction"] = ""
        item["input"] = item["content"]
    for item in test_data:
        item["instruction"] = ""
        item["input"] = item["content"]


    train_org_file = data_file_path +"/train_org.json"
    # 获取目录路径
    dir_path = os.path.dirname(train_org_file)
    # 如果目录不存在，则创建目录
    os.makedirs(dir_path, exist_ok=True)
    os.chmod(dir_path, 0o755)
    with open(train_org_file, 'w', encoding='utf-8') as file:
        json.dump(train_data, file, indent=4)

    test_org_file = data_file_path + "/test_org.json"
    # 获取目录路径
    dir_path = os.path.dirname(test_org_file)

    # 如果目录不存在，则创建目录
    os.makedirs(dir_path, exist_ok=True)
    os.chmod(dir_path, 0o755)
    with open(test_org_file, 'w', encoding='utf-8') as file:
        json.dump(test_data, file, indent=4)


if __name__ == "__main__":
    csv_file_path = "financialNews.csv"
    news = convert_to_llama(csv_file_path)
    print("数据转换完成。")

    # 使用示例
    seed_list = [42]
    for seed in seed_list:
        data_file_path = "../../data/fin/SEntFiN"
        # data_file_path = "../../data/fin/SEntFiN/"+ "seed" + str(seed)

        split_data(seed, news, data_file_path)
    print("数据分割完成。")

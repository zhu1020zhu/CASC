import json
import random

import re

def convert_to_llama(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        news=[]
        i=0

        for entry in data:
            new={}
            content = entry.get('content', '')
            annotations = entry.get('annotations', [])
            new_aanos = []

            for annotation in annotations:
                new_aano = {}
                new_aano["value"] = annotation["value"]
                new_aano["start"] = annotation["start"]
                new_aano["end"] = annotation["end"]
                new_aano["tag"] = annotation["tag"]

                new_aano = json.dumps(new_aano)
                # print(new_aano)
                new_aanos.append(new_aano)
            
            
            output = ""
            # print(len(annotations))
            if len(new_aanos)==1:
                output = str(new_aanos[0])
            else:
                output = str(new_aanos[0])
                for new_anno in new_aanos[1:]:
                    output = output+"\n"+str(new_anno)

            new["id"] = i
            i=i+1
            new["content"] = content
            new["input"] = ""
            new["output"] = output
            news.append(new)
        return news

def split_data(news, data_file_path, train_ratio=0.8):

    data = news

    total_size = len(data)
    train_size = int(total_size * train_ratio)

    # 随机打乱数据
    random.shuffle(data)

    # 分割数据
    train_data = data[:train_size]
    test_data = data[train_size:]

    # 写入分割后的数据到相应文件
    # train_file = data_file_path + "random_train.json"
    # with open(train_file, 'w', encoding='utf-8') as file:
    #     json.dump(train_data, file, indent=4)
    #
    # test_file = data_file_path + "random_test.json"
    # with open(test_file, 'w', encoding='utf-8') as file:
    #     json.dump(test_data, file, indent=4)

    for item in train_data:
        item["instruction"] = ""
        item["input"] = item["content"]
    for item in test_data:
        item["instruction"] = ""
        item["input"] = item["content"]


    train_org_file = data_file_path + "train_org.json"
    with open(train_org_file, 'w', encoding='utf-8') as file:
        json.dump(train_data, file, indent=4)

    test_org_file = data_file_path + "test_org.json"
    with open(test_org_file, 'w', encoding='utf-8') as file:
        json.dump(test_data, file, indent=4)


if __name__ == "__main__":
    json_file_path = "FinEntity.json"
    data_file_path = "../../data/fin/FinEntity/"

    news = convert_to_llama(json_file_path)
    print("数据转换完成。")

# 使用示例
    split_data(news, data_file_path)
    print("数据分割完成。")

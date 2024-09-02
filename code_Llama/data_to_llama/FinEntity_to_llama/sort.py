import json
import random

import re


def read_jsonfile(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data



def sort_out(data):
    for item in data:
        output = item["output"].split("\n")

        json_output = []
        for anno in output:
            json_anno = json.loads(anno)
            json_output.append(json_anno)
        sort_json_output1 = sorted(json_output, key=lambda x: x['start'])  # 按start值对每组排序

        sort_json_output = []
        for anno in sort_json_output1:
            anno = json.dumps(anno)  # 保证双引号。
            sort_json_output.append(anno)

        if len(sort_json_output) == 1:
            sort_output = str(sort_json_output[0])
        else:
            sort_output = str(sort_json_output[0])
            for sort_item in sort_json_output[1:]:
                sort_output = sort_output + "\n" + str(sort_item)
        item["output"] = sort_output
    return data

def write_jsonfile(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    json_file_path = "../../data/fin/record/"
    data_file_path = "../../data/fin/FinEntity/"

    train_data = read_jsonfile(json_file_path+"train_org.json")
    sort_train_data = sort_out(train_data)
    write_jsonfile(sort_train_data, data_file_path+"train_org.json")

    test_data = read_jsonfile(json_file_path+"test_org.json")
    sort_test_data = sort_out(test_data)
    write_jsonfile(sort_test_data, data_file_path+"test_org.json")

    print("数据转换完成。")
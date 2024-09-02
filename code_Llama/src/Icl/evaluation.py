import json

from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
import time
import pandas as pd
import re
import random
from tqdm import tqdm
from Icl.predict import Model

def get_metric(y_trues, y_preds, id=None):
    y_true_binarys, y_pred_binarys = [], []
    for y_true, y_pred in zip(y_trues, y_preds):
        # print(y_pred)
        # 先把所有出现的元组进行合并
        if id != None:
            # 计算单个元素的指标
            y_true_set = set(item[id] for item in y_true)
            y_pred_set = ()
            for item in y_pred:
                # 防止预测结果不足
                if len(item) >= id+1:
                    y_pred_set += (item[id],)
            # y_pred_set = set(item[id] for item in y_pred)
        else:
            y_true_set = set(str(item) for item in y_true)
            y_pred_set = set(str(item) for item in y_pred)
        all_tuples = y_true_set.union(y_pred_set)

        # 转换为 0-1 表示形式
        y_true_binary = [1 if item in y_true_set else 0 for item in all_tuples]
        y_pred_binary = [1 if item in y_pred_set else 0 for item in all_tuples]

        y_true_binarys.extend(y_true_binary)
        y_pred_binarys.extend(y_pred_binary)

    # 计算指标
    accuracy = accuracy_score(y_true_binarys, y_pred_binarys)
    precision = precision_score(y_true_binarys, y_pred_binarys)
    recall = recall_score(y_true_binarys, y_pred_binarys)
    f1 = f1_score(y_true_binarys, y_pred_binarys)

    return accuracy, precision, recall, f1

def get_metrics(y_trues, y_preds, task):
    # 计算各个子任务的指标
    acc, p, r, f1 = get_metric(y_trues, y_preds)
    
    print(f"{task} Accuracy: {acc:.4f} Precision: {p:.4f} Recall: {r:.4f} F1 Score: {f1:.4f}")
    items_dict = {0: 'Aspect', 1: 'Sentiment'}
    for k, v in items_dict.items():
        acc, p, r, f1 = get_metric(y_trues, y_preds, id=k)
        print(f"{v} Accuracy: {acc:.4f} Precision: {p:.4f} Recall: {r:.4f} F1 Score: {f1:.4f}")

def parse_output(s):

    groups = s.split('\n')
    elements = []
    for group in groups:
        element = []
        json_group = json.loads(group)
        element.append(json_group["value"])
        element.append(json_group["tag"])
        elements.append(element)
    # elements = [re.split(r',\s*', group) for group in groups]
    return elements

def evaluate(base_model_path, test_data, task, checkpoint_dir, temperature=0.1, top_p=0.9, finetuning_type="lora"):
    model = Model(base_model_path, checkpoint_dir, temperature, top_p, finetuning_type)

    y_trues, y_preds = [], []
    damain_labels = {}
    error_records = []  # 用于保存错误的记录
    save_pres = []
    # for data in tqdm(random.sample(test_data, 100)):
    for data in tqdm(test_data):
        instruction = data['instruction']

        pred = model.generate(instruction)
        true = data['output']
        
        try:
            pred_list = parse_output(pred)
            true_list = parse_output(true)
        
        except Exception as e:
            # 如果在生成或解析预测过程中出现异常，将预测结果设置为异常信息，将预测结果设置为空列表
            pred = str(e)
            pred_list = []
        save_pre = {}
        save_pre["id"] = data["id"]
        save_pre["instruction"] = data["instruction"]
        save_pre["content"] = data["content"]
        save_pre["output"] = data["output"]
        save_pre["pre"] = pred
        save_pres.append(save_pre)


        y_trues.append(true_list)
        y_preds.append(pred_list)
                
        # # 每个领域的预测结果
        # if data['domain'] not in damain_labels:
        #     damain_labels[data['domain']] = {'pred': [], 'true': []}
        # else:
        #     damain_labels[data['domain']]['pred'].append(pred_list)
        #     damain_labels[data['domain']]['true'].append(true_list)

        # 如果预测的输出与真实的输出不匹配，将它们添加到错误记录中
        if pred != true:
            error_records.append({
                'id': data['id'],
                'instruction': instruction,
                'true': true,
                'predict': pred, 
            })
    if(task=="FinEntity"):
        save_path = f"./results_FinEntity/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"
    elif(task=="SEntFiN"):
        save_path = f"./results_SEntFiN/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"
    elif (task == "EFSA"):
        save_path = f"./results_EFSA/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"
    elif (task == "FinEntity_correct"):
        save_path = f"./results_correct/FinEntity_correct/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"
    elif (task == "SEntFiN_correct"):
        save_path = f"./results_correct/SEntFiN_correct/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"
    elif (task == "EFSA_correct"):
        save_path = f"./results_correct/EFSA_correct/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"
    else:
        save_path = f"./results2/save_pres_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json"

    with open(save_path, 'wt') as f:
        print(json.dumps(save_pres), file=f)
    print("预测结果保存完成，路径：", save_path)

    # 计算总的效果
    get_metrics(y_trues, y_preds, task=task)
    # # 每个领域的效果
    # for domain, labels in damain_labels.items():
    #     print(f"Domain: {domain}")
    #     get_metrics(labels['true'], labels['pred'], task=task)

    # 保存错误记录到CSV
    if error_records:
        df_errors = pd.DataFrame(error_records)
        if (task == "FinEntity"):
            error_path = f"./results_FinEntity/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        elif (task == "SEntFiN"):
            error_path = f"./results_SEntFiN/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        elif (task == "EFSA"):
            error_path = f"./results_EFSA/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        elif (task == "FinEntity_correct"):
            error_path = f"./results_correct/FinEntity_correct/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        elif (task == "SEntFiN_correct"):
            error_path = f"./results_correct/SEntFiN_correct/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        elif (task == "EFSA_correct"):
            error_path = f"./results_correct/EFSA_correct/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        else:
            error_path = f"./results2/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        # error_path = f"./results2/error_records_{task}_{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.csv"
        df_errors.to_csv(error_path, index=False, sep='\t')
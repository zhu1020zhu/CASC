import json
import torch
import random
from Icl.templates import *
from Icl.ex_retriver import Ex_Retriver
from tqdm import tqdm

domain_dict = {'14lap':'laptop', '14res':'restaurant', '14twitter':'twitter', 'books':'books', 'clothing':'clothing', 
        'device':'device', 'financial':'finance', 'hotel':'hotel', 'mets-cov':'COVID', 'service': 'service'}

def construct_instruct(json_path, save_path, top_k, ICL, retriever=None, task='ASPE',  verbose=False):
    '''
    json_path: 原始，需要建立索引的数据路径
    save_path: 保存的路径
    '''
    sents, labels = [], []
    with open(json_path, 'r', encoding='UTF-8') as fp:
        data = json.load(fp)
        for d in tqdm(data):
            if task == 'FinEntity':
                if ICL=="icl":
                    examples = retriever.search_examples(d['input'], top_k, verbose=verbose)

                    examples_str = ""
                    for id, example in enumerate(examples):
                        examples_str += f'Example {id+1}:\nInput: "{example[0]}"\nOutput: "{example[1]}"\n'

                    prompt = random.choice(FinEntity_icl_templates).format(example=examples_str, input=d['input'])
                elif ICL == "fixicl":
                    prompt = random.choice(FinEntity_fixicl_templates) + d['input'] + "\nOutput:\n"
                else:
                    prompt = random.choice(FinEntity_templates).format(input=d['input'])

            elif task == 'FinEntity_correct':
                if ICL == "icl":
                    examples = retriever.search_examples(d['content'], top_k, verbose=verbose)

                    examples_str = ""
                    for id, example in enumerate(examples):
                        examples_str += f'Example {id + 1}:\nSentence: "{example[0]}"\nPseudo-labels: "{example[1][1]}"\nOutput: "{example[1][0]}"\n'

                    prompt = random.choice(FinEntity_correct_icl_templates).format(example=examples_str,
                                                                                   content=d["content"], pre=d["pre"])
                elif ICL == "fixicl":
                    # print(d["content"])
                    # print(random.choice(SEntFiN_correct_templates))
                    prompt = random.choice(FinEntity_correct_templates).format(content=d["content"], pre=d["pre"])
                else:
                    prompt = random.choice(FinEntity_correct_templates).format(content=d["content"], pre=d["pre"])

            elif task == 'SEntFiN':
                if ICL=="icl":
                    examples = retriever.search_examples(d['input'], top_k, verbose=verbose)

                    examples_str = ""
                    for id, example in enumerate(examples):
                        examples_str += f'Example {id+1}:\nInput: "{example[0]}"\nOutput: "{example[1]}"\n'

                    prompt = random.choice(SEntFiN_icl_templates).format(example=examples_str, input=d['input'])
                elif ICL == "fixicl":
                    prompt = random.choice(SEntFiN_fixicl_templates) + d['input'] + "\nOutput:\n"
                else:
                    prompt = random.choice(SEntFiN_templates).format(input=d['input'])

            elif task == 'SEntFiN_correct':
                if ICL == "icl":
                    examples = retriever.search_examples(d['content'], top_k, verbose=verbose)

                    examples_str = ""
                    for id, example in enumerate(examples):
                        examples_str += f'Example {id + 1}:\nSentence: "{example[0]}"\nPseudo-labels: "{example[1][1]}"\nOutput: "{example[1][0]}"\n'

                    prompt = random.choice(SEntFiN_correct_icl_templates).format(example=examples_str,
                                                                                 content=d["content"], pre=d["pre"])
                elif ICL == "fixicl":
                    # print(d["content"])
                    # print(random.choice(SEntFiN_correct_templates))
                    prompt = random.choice(SEntFiN_correct_templates).format(content=d["content"], pre=d["pre"])
                else:
                    prompt = random.choice(SEntFiN_correct_templates).format(content=d["content"], pre=d["pre"])

            elif task == 'EFSA':
                if ICL=="icl":
                    examples = retriever.search_examples(d['input'], top_k, verbose=verbose)

                    examples_str = ""
                    for id, example in enumerate(examples):
                        examples_str += f'Example {id+1}:\nInput: "{example[0]}"\nOutput: "{example[1]}"\n'

                    prompt = random.choice(EFSA_icl_templates).format(example=examples_str, input=d['input'])
                elif ICL == "fixicl":
                    prompt = random.choice(EFSA_fixicl_templates) + d['input'] + "\nOutput:\n"
                else:
                    prompt = random.choice(EFSA_templates).format(input=d['input'])


            else:
                raise NotImplementedError

            d['instruction'] = prompt
            d['input'] = ""

    # 直接将数据保存到对应位置
    with open(save_path, 'w', encoding='UTF-8') as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)

prefix = './data'
data_files = {
    'EFSA': '/fin/EFSA/',
    'SEntFiN': '/fin/SEntFiN/',
    'FinEntity': '/fin/FinEntity/',
    'SEntFiN_correct': '/train_pre/SEntFiN/',
    'EFSA_correct': '/train_pre/EFSA/',
    'FinEntity_correct': '/train_pre/FinEntity/',
    'ASPE': '/ASPE/',
    'MEMD_AS': '/MEMD/AS/',
    'MEMD_AOS': '/MEMD/AOS/',
    'MEMD_ACOS': '/MEMD/ACOS/',
}

def data_process(top_k, task, ICL, paths, method):
    if task not in ['EFSA', 'SEntFiN', 'FinEntity', 'EFSA_correct', 'SEntFiN_correct', 'FinEntity_correct', 'ASPE', 'MEMD_AS', 'MEMD_AOS', 'MEMD_ACOS']:
        raise NotImplementedError

    train_org_path = prefix + data_files[task] + 'train_org.json'
    train_path = prefix + data_files[task] + method + '_train.json'
    test_org_path = prefix + data_files[task] + 'test_org.json'
    test_path = prefix + data_files[task] + method + '_test.json'

    if ICL=="icl":
        if method == 'random':
            retriever = Ex_Retriver(ex_file=train_org_path, encode_method='random')
            construct_instruct(train_org_path, train_path, top_k, ICL, retriever, task=task, )
            construct_instruct(test_org_path, test_path, top_k, ICL, retriever, task=task, )
        elif method == 'sbert':
            retriever = Ex_Retriver(ex_file=train_org_path, paths=paths, encode_method='sbert')
            construct_instruct(train_org_path, train_path, top_k, ICL, retriever, task=task,)
            construct_instruct(test_org_path, test_path, top_k, ICL, retriever, task=task,)
            # 清除模型释放显存
            del retriever
        elif method == 'gnn':
            retriever = Ex_Retriver(ex_file=train_org_path, paths=paths, encode_method='gnn')
            construct_instruct(train_org_path, train_path, top_k, ICL, retriever, task=task,)
            construct_instruct(test_org_path, test_path, top_k, ICL, retriever, task=task, verbose=False)
            del retriever
        else:
            raise NotImplementedError
    elif ICL=="fixicl":
        construct_instruct(train_org_path, train_path, top_k, ICL, task=task)
        construct_instruct(test_org_path, test_path, top_k, ICL, task=task)
    else:
        construct_instruct(train_org_path, train_path, top_k, ICL, task=task)
        construct_instruct(test_org_path, test_path, top_k, ICL, task=task)

    torch.cuda.empty_cache()

    with open(test_path, 'r', encoding='utf-8') as f:
        test_data = json.load(f)

    return test_data

# construct_instruct('/hy-tmp/workspace/SA-LLM/data/inst/ASPE/test_org.json', '/hy-tmp/workspace/SA-LLM/data/inst/ASPE/test.json', ICL=False)

#!/bin/bash
source /home/zhubin/anaconda3/etc/profile.d/conda.sh
conda activate llamaPy3.8
set -ex

#echo "abck" |tee -a ./results/result.txt

#python ./src/main.py \
#    --task FinEntity \
#    --method noicl \
#    --do_train \
#    --seed 42 \
#    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf/ \
#    --finetuning_type lora \
#    --lora_rank 128 \
#    --per_device_train_batch_size 16 \
#    --per_device_eval_batch_size 16 \
#    --gradient_accumulation_steps 4 \
#    --logging_steps 20 \
#    --save_steps 100 \
#    --val_size 0.1 \
#    --learning_rate 8e-5 \
#    --num_train_epochs 5.0 \
#    --fp16

#python ./src/main.py \
#    --task FinEntity \
#    --method fixicl \
#    --do_train \
#    --seed 42 \
#    --top_k 3 \
#    --num_train_epochs 5 \
#    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf-finance/ \
#    --finetuning_type lora \
#    --lora_rank 128 \
#    --per_device_train_batch_size 4 \
#    --per_device_eval_batch_size 4 \
#    --gradient_accumulation_steps 4 \
#    --logging_steps 60 \
#    --save_steps 100 \
#    --val_size 0.1 \
#    --learning_rate 8e-5 \
#    --num_train_epochs 5.0 \
#    --fp16

#python ./src/main.py \
#    --task FinEntity \
#    --method random \
#    --do_train \
#    --seed 42 \
#    --top_k 4 \
#    --num_train_epochs 5 \
#    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf/ \
#    --finetuning_type lora \
#    --lora_rank 128 \
#    --per_device_train_batch_size 4 \
#    --per_device_eval_batch_size 4 \
#    --gradient_accumulation_steps 4 \
#    --logging_steps 60 \
#    --save_steps 100 \
#    --val_size 0.1 \
#    --learning_rate 8e-5 \
#    --num_train_epochs 5.0 \
#    --fp16

#python ./src/main.py \
#    --task FinEntity \
#    --method random \
#    --do_train \
#    --seed 42 \
#    --top_k 5 \
#    --num_train_epochs 5 \
#    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf/ \
#    --finetuning_type lora \
#    --lora_rank 128 \
#    --per_device_train_batch_size 4 \
#    --per_device_eval_batch_size 4 \
#    --gradient_accumulation_steps 4 \
#    --logging_steps 60 \
#    --save_steps 100 \
#    --val_size 0.1 \
#    --learning_rate 8e-5 \
#    --num_train_epochs 5.0 \
#    --fp16


#python ./src/main.py \
#    --task SEntFiN \
#    --method fixicl \
#    --do_train \
#    --seed 42 \
#    --top_k 3 \
#    --num_train_epochs 5 \
#    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf-finance/ \
#    --finetuning_type lora \
#    --lora_rank 128 \
#    --per_device_train_batch_size 4 \
#    --per_device_eval_batch_size 4 \
#    --gradient_accumulation_steps 4 \
#    --logging_steps 60 \
#    --save_steps 100 \
#    --val_size 0.1 \
#    --learning_rate 8e-5 \
#    --num_train_epochs 5.0 \
#    --fp16

#CUDA_VISIBLE_DEVICES=3 \
#python ./src/main.py \
#    --task FinEntity_correct \
#    --method gnn \
#    --do_train \
#    --seed 42 \
#    --top_k 3 \
#    --num_train_epochs 5 \
#    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf-finance/ \
#    --finetuning_type lora \
#    --lora_rank 128 \
#    --per_device_train_batch_size 4 \
#    --per_device_eval_batch_size 4 \
#    --gradient_accumulation_steps 4 \
#    --logging_steps 60 \
#    --save_steps 100 \
#    --val_size 0.1 \
#    --learning_rate 8e-5 \
#    --num_train_epochs 5.0 \
#    --fp16


CUDA_VISIBLE_DEVICES=3 \
python ./src/main.py \
    --task SEntFiN_correct \
    --method gnn \
    --do_train \
    --seed 42 \
    --top_k 3 \
    --num_train_epochs 5 \
    --model_name_or_path /home/zhubin/WorkSpace/Models/Llama-2-7b-hf-finance/ \
    --gnn_path /home/zhubin/WorkSpace/Finllm_fin_3090/checkpoints/gnn/sentfin_correct/best_gnn_model.pt \
    --bert_path /home/zhubin/WorkSpace/Models/bert-base-uncased \
    --finetuning_type lora \
    --lora_rank 128 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 8 \
    --logging_steps 100 \
    --save_steps 100 \
    --val_size 0.1 \
    --learning_rate 8e-5 \
    --num_train_epochs 5.0 \
    --fp16
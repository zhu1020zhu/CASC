
#CUDA_VISIBLE_DEVICES=3 python src/gnnencoder/train.py \
#    --task FinEntity \
#    --save_path ./checkpoints/gnn/finentity/ \
#    --batch_size 128 \
#    --max_len 128 \
#    --epoch_num 10 \
#    --lr 1e-4 \
#    --lig_threshold 0.37 \
#    --sent_threshold 0.8

CUDA_VISIBLE_DEVICES=2 python src/gnnencoder/train.py \
    --task SEntFiN \
    --save_path ./checkpoints/gnn/sentfin/ \
    --batch_size 128 \
    --max_len 128 \
    --epoch_num 10 \
    --lr 1e-4 \
    --lig_threshold 0.46 \
    --sent_threshold 0.8

#CUDA_VISIBLE_DEVICES=3 python src/gnnencoder/train.py \
#    --task ASPE \
#    --save_path ./checkpoints/gnn/aspe/ \
#    --batch_size 128 \
#    --max_len 128 \
#    --epoch_num 10 \
#    --lr 1e-4 \
#    --lig_threshold 0.43 \
#    --sent_threshold 0.8

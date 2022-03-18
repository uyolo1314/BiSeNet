
## bisenetv2
cfg = dict(
    model_type='bisenetv2',
    n_cats=2,
    num_aux_heads=4,
    lr_start=5e-3,
    weight_decay=1e-4,
    warmup_iters=1000,
    max_iter=60000,
    dataset='Expressage',
    im_root='',
    train_im_anns='/project/train/src_repo/dataset/train.txt',
    val_im_anns='/project/train/src_repo/dataset/val.txt',
    scales=[0.75, 2.],
    cropsize=[640, 640],
    eval_crop=[640, 640],
    eval_scales=[0.5, 0.75, 1, 1.25, 1.5, 1.75],
    ims_per_gpu=8,
    eval_ims_per_gpu=1,
    use_fp16=True,
    use_sync_bn=True,
    respth='/project/train/models',
)

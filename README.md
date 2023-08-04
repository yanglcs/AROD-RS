# AROD-RS


The full code will be released later...


#### Training
```bash
python train_robust.py --cfg cfgs/RobustDet_hrsc.yaml --adv_type mtd(or cwat) --data_use clean --multi_gpu False \
    --basenet <path_to_weights> --dataset_root <path_to_your_hrsc_root>
```

#### Evaluation
```bash
python eval_attack.py --cfg cfgs/RobustDet_hrsc.yaml --trained_model <path_to_your_trained_model> \
    --data_use clean --adv_type cls \ # attack type, choice in [clean, cls, loc, cwat, dag]
     --dataset_root <path_to_your_hrsc_root>
```

## Acknowledgment

This repository is built based on [RobustDet](https://github.com/7eu7d7/RobustDet), [ODConv](https://github.com/OSVAI/ODConv) repositories. We thank the authors for releasing their amazing codes.



# Towards Attack to MemGuard With Non-Local-means Method
We use the non-local-method to attack the [MemGuard](https://arxiv.org/abs/1909.10594). We remove the noise added by the MemGuard scheme using the idea of the classical [non-local-means method](https://ieeexplore.ieee.org/abstract/document/1467423). We use the three datasets to prove the effectiveness of our attack, including Location, Texas100 and CH-MNIST as used in MemGuard. 
## Experimental result
## Code usage
The code mainly include the process of denoising. Using the process of denoising, we can remove the noise added by MemGuard, the result of our experiments prove our conclusion.
## Citation
If you use this code or dataset, please cite following paper:
```
@inproceedings{Xie2021attack_1,
  title={Towards Attack to the Adversarial Example Based Privacy Protection Schemes},
  author={Guangxu Xie},
  booktitle={Security and Communication Networks},
  year={2021}
}
```


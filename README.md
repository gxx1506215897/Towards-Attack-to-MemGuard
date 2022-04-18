# Towards Attack to MemGuard With Non-Local-means Method
We employ 0-norm projected gradient descent (PGD) for adversarial training (AT), while using simple random sampling to train a more robust attack model for attacking [AttriGuard](https://arxiv.org/abs/1805.04810). We conduct experiments using the AttriGuard dataset, and the experimental results demonstrate the effectiveness of the attack.
## Experimental result
<p float="left">
  <img src="https://github.com/gxx1506215897//location.png" alt='images' width="250"/>
</p>

We used 7 attack methods to attack AttriGuard. The attack structure is shown in Fig. In the process of increasing the data loss budget, the inference accuracy of our attack decreases more slowly relative to the attack in AttriGuard. The experimental results show that our attack is effective.

## Code usage
The code mainly include the process of denoising. Using the process of denoising, we can remove the noise added by MemGuard, the result of our experiments prove our conclusion. To test the effectiveness of our attack, you have to load the code of [MemGuard](https://github.com/jjy1994/MemGuard). If you have any question, please feel free to send email to guangxxie@126.com.
## Citation
If you use this code or dataset, please cite following paper:
```
@inproceedings{Xie2021attack_2,
  title={Towards Attack to MemGuard With Non-Local-means Method},
  author={Guangxu Xie, Qingqi Pei},
  booktitle={Security and Communication Networks},
  year={2021}
}
```


# EfficientFormer

This repository evaluates and compares various efficient transformer models using the [Long Range Arena](https://arxiv.org/abs/2011.04006). In particular, we investigate the impact of alternative sampling methods on the performance and computational efficiency of [Reformer](https://arxiv.org/abs/2001.04451) and [HyperAttention](https://arxiv.org/html/2310.05869v3) methods.

The backbone of this repository is built off the [official implementation](https://github.com/pkuzengqi/Skyformer) of [Skyformer](https://arxiv.org/abs/2111.00035) and the [official implementation](https://github.com/insuhan/hyper-attn/) of [HyperAttention](https://arxiv.org/html/2310.05869v3).

## Requirements

A conda environment with the necessary packages can be setup using `efficientformer.yml`:

```shell
conda env create --file efficientformer.yml
conda activate efficientformer
```

Alternatively, the  listed in ```requirements.txt```.

## Data Preparation

There are two alternative methods for setting up the data.

Processed files can be downloaded [here](https://drive.google.com/drive/folders/1rE0SjpeFKPFtgmWWjYCoIMz91UozHWWC?usp=sharing), or processed with the following steps:

1. Activate environment

```shell
conda activate efficientformer
```

2. Download [the TFDS files for pathfinder](https://storage.cloud.google.com/long-range-arena/pathfinder_tfds.gz) and then set _PATHFINER_TFDS_PATH to the unzipped directory as outlined in [here](https://github.com/google-research/long-range-arena/issues/11).
3. Download [lra_release.gz](https://storage.googleapis.com/long-range-arena/lra_release.gz) (7.7 GB).
4. Unzip `lra-release` and put under `./data/`

```shell
cd data
wget https://storage.googleapis.com/long-range-arena/lra_release.gz
tar zxvf lra-release.gz 
```

5. Create a directory `lra_processed` under `./data/`

```shell
mkdir lra_processed
cd ..
```

6. The directory structure would be (assuming the root dir is `code`)

```shell
./data/lra-processed
./data/long-range-arena-main
./data/lra_release
```

7. Create train, dev, and test dataset pickle files for each task

```shell
cd preprocess
python create_pathfinder.py
python create_listops.py
python create_retrieval.py
python create_text.py
python create_cifar10.py
```

Note: most source code comes from [LRA repo](https://github.com/google-research/long-range-arena).

## Run

Modify the configuration in `config.py` and run

```shell
python main.py --mode train --attn skyformer --task lra-text
```

- mode: `train`, `eval`
- attn: `softmax`, `nystrom`, `linformer`, `reformer`, `perfromer`, `informer`, `bigbird`,  `kernelized`, `skyformer`
- task: `lra-listops`, `lra-pathfinder`, `lra-retrieval`, `lra-text`, `lra-image`

## Reference

```bibtex
@inproceedings{Skyformer,
    title={Skyformer: Remodel Self-Attention with Gaussian Kernel and Nystr\"om Method}, 
    author={Yifan Chen and 
            Qi Zeng and 
            Heng Ji and 
            Yun Yang},
    booktitle={Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December
               6-14, 2021, virtual},
    year={2021}
}

```

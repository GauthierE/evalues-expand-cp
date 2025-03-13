# evalues-expand-cp

This repository contains the code for reproducing the experiments and figures presented in the paper [E-values Expand the Scope of Conformal Prediction]([https://arxiv.org/abs/2502.04879](https://github.com/)).

## Organization

The repository is structured into three main folders, each corresponding to one of the three methods presented in the paper: batch anytime-valid conformal prediction (`batch-anytime-valid-cp`), fixed-size conformal sets (`fixed-size-conformal-sets`), and conformal prediction under ambiguous ground truth (`monte-carlo-cp`). Each folder is self-contained and independent of the others.

## Instructions

### Batch anytime-valid conformal prediction

1. Run the `load_dataset.ipynb` notebook. This will generate a `femnist.csv` file.

2. Run the `split_dataset.ipynb` notebook. This will create 2 files: `train.csv` (training set) and `test.csv` (test set).

3. (*Optional*) Run the `model_train.ipynb` notebook to re-train the model f. The training weights will be saved in the `weights/` folder, and the training history will be stored in the `results/` folder.

4. Execute the `batch-anytime-valid-cp.ipynb` notebook to reproduce the experiments from the paper.

### Fixed-size conformal sets

1. Run the `load_dataset.ipynb` notebook. This will generate a `femnist.csv` file.

2. Run the `split_dataset.ipynb` notebook. This will create 2 files: `train.csv` (training set) and `test.csv` (test set).

3. (*Optional*) Run the `model_train.ipynb` notebook to re-train the model f. The training weights will be saved in the `weights/` folder, and the training history will be stored in the `results/` folder.

4. Execute the `fixed-size-cp.ipynb` notebook to reproduce the experiments from the paper.

### Conformal prediction under ambiguous ground truth

1. Manually download the two files `cifar10h-counts.npy` and `cifar10h-probs.npy` from the [CIFAR-10H dataset](https://github.com/jcpeterson/cifar-10h/tree/master/data) and place them in the `data/` folder.

2. Manually download the file `cifar-10-python.tar.gz` from the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html) and add it to the `data/` folder. *This step should be automatically performed when running either `model_train.ipynb` or `monte-carlo-cp.ipynb`*.

3. Execute the `monte-carlo-cp.ipynb` notebook to reproduce the experiments from the paper.

4. Visualize the results using the `plot.ipynb` notebook.

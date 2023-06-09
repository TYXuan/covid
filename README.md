# Detection of COVID-19 in Chest X-rays

By Tan Yu Xuan

email: yxtan05@gmail.com


## Project Organisation


    ├── run.sh             <- .sh file which preprocesses the raw data and performs predictions.
    |
    ├── README.md          <- The top-level README for users of this project.
    |
    ├── data               <- Where heart.csv should be placed in & processed results are stored in.
    | 
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    |
    ├── eda.ipynb          <- Exploratory data analysis.
    |
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │   
        |── dataprocessing.py <- Script to ingest and process dataset
        |
        |── modeling.py    <- Script to perform predictions based on processed dataset.
        |
        |── data           <- Scripts to download or generate data
        |     └── make_dataset.py
        |
        └── models         <- Dumps of trained models
              └── cnn_model.hdf5
--------

# Instructions

## 1. Setting up the enviroment

### Install the required libraries from your terminal

- In your command shell/terminal locate the directory where requirements.txt is located and type in the following:

      conda create --name covid --file requirements.txt

### Once all packages/libraries are installed activate the installed enviroment

- Key in the following code into your shell:

      conda activate covid

## 2. Running the model

- In your command shell/terminal move to where run.sh is located and key in the following command
    
      ./run.sh
--------

# Engineering Pipeline

1. Import dataset
2. Checking for duplicates & missing values
3. Saving processed dataset out as .csv
4. Convert images into arrays
5. One-hot encode image labels
6. Fit augmented model & save as .hdf5 file
7. Predict original images with model
8. Output results in .csv file

# EDA Overview

The EDA contains overview of key findings from the dataset. Choices made in the pipeline are based on those findings, particularly any feature engineerings for modelling. Please keep the details of the EDA in the `.ipynb` which serves as a quick summary.

# Model

CNN model is used for this project.

# Model Evaluation

For classification models the baseline was set to an accuracy of 0.5 where the model has a 50:50 chance of a correct prediction.
The goal is for our models to perform better than a coin toss.

We will be looking at the recall of the images labelled 'covid' and 'pneumonia' as they are both contagious.

### Scoring metrics
**Accuracies**

| model | training set | validation set |
|-------|--------------|----------------|
|  CNN  |    0.83      |      0.87      |

Based on the validation set, the CNN model has a 86% chance of identifying the correct label which is better than our baseline.

Comparing the scores from the training set and test set, there might be some underfitting has the model performs better on the validation data.

### a. Confusion Matrix
|              | covid | normal | pneumonia |
|--------------|-------|--------|-----------|
| covid        | `128` |   11   |     3     |
| normal       |   27  |  `89`  |     10    |
| pneumonia    |   0   |   1    |    `135`  |

### b. Classification Report

| label     | precision | recall | f1-score|
|-----------|-----------|--------|---------|
| covid     |  0.83     | `0.90` |   0.86  |
| normal    |  0.88     |  0.71  |   0.85  |
| pneumonia |  0.91     | `0.99` |   0.90  |

Based on the classification report, the CNN model is better at identifying image labbelled 'covid' and 'pneumonia'.

# Conclusion
In the case of model predicting COVID-19 postives, it is desired to have a very high recall than precision.
In other words, it is important to minimise the False Negatives for 'covid' and 'pneumonia' which is the cases predicted negative but are not actually negative.
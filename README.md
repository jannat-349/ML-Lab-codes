# Machine Learning Guide

## Overview

This repository serves as a guide to various machine learning techniques. Each commit represents a significant milestone in the project.

## Commits

### Commit 1: Decision Tree Implementation
- **Algorithms Used:** ID3 and CART
- **Accuracy:** 100%

| New day 15 | New day 16 |
|---|---|
|![349_Jannat_decision_tree_page-0002](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/a0ff4a64-9b9e-4434-8d63-3e59f982d35f)|![349_Jannat_decision_tree_page-0003](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/43728826-c6d0-4a37-a8a6-3c5f23d02139)|

### Commit 2: Data Visualization with WEKA
- Download and install Weka
- Getting started with Weka
- Visualize your data from the Weka Dataset
- Handle missing values
- Handle outliers and extreme values
- Classification using Weka
- Visualize result in Weka

### Commit 5: Linear Regression
It predicts weight in kg for a given height in cm.
- **Mean Square Error:** 4.16

Output:

![image](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/1428b0c7-863f-4a1d-a405-9fae2c4409eb)

### Commit 7: Predicting Stroke using XGBoost Algorithm
It predicts stroke based on some physical conditions. At first preprocessed the data, then applied XGBoost using 10 fold cross validation. Combined all the confusion matrices and lastly calcualted some evaluation parameters.

Input: stroke_prediction_dataset.csv (size: 15k)

Output:
- **Accuracy:** 0.49853333333333333
- **Precision:** 0.5004963271788763
- **Recall:** 0.6694105151354222
- **F1 Score:** 0.5727592866068385
- **Specificity:** 0.32619175147295126
- **False Positive Rate:** 0.6738082485270488
- **ROC AUC:** 0.5237049648690493


| Dataset Before Preprocessing | 
|--|
| ![image](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/965c7078-b4c0-4d2b-89e8-d5ee36635d38) |

| Dataset After Preprocessing |
|--|
| ![image](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/dc979c09-c723-42bb-b684-94e0d6fcf8c9) |

|Confusion Matrix | Evaluation Metrics|
|--|--|
| ![image](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/89f49c7d-617c-495a-aadd-f4331f22d6d9) | ![xgboost](https://github.com/jannat-349/ML-Lab-codes/assets/50805240/e998389a-e360-4a29-ad0b-b58928f0e649) |




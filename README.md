# PredCaII
### Integrated hierarchical fusion of GRU and meta-features for enhanced identification and interpretation of calcium ion inhibitors

The movement of calcium ions across cell membranes is vital for processes such as hormone release, electrical signaling, and epithelial and cellular function. Calcium ion inhibitors have therapeutic potential for treating conditions like cancer, cardiac arrhythmias, and endocrine disorders. This study presents a neural network-based model to identify such inhibitors using a hybrid feature engineering and ensemble learning approach. Seven peptide encoding methods and five machine learning classifiers were used to generate 35 base models. Probabilistic and class label outputs from these models were combined into a 70-dimensional vector. Additionally, peptide sequences were encoded with the AAindex matrix, and a gated recurrent unit (GRU) extracted long-range features, resulting in another 70-dimensional vector. These were merged into a 140-dimensional feature vector and input into a two-layer multilayer perceptron classifier. The model outperformed baselines and existing methods. Interpretability tools like SHAP and Integrated Gradients revealed key biochemical and structural factors influencing predictions.

<br>
<br>

# Requirments
### 1. scikit-learn:   1.5.1
### 2. xgboost:   3.0.0
### 3. lightgbm:   4.6.0
### 4. optuna:   4.3.0
### 5. shap:  0.48.0
### 6. torch:  2.2.0+cu118
### 7. captum:  0.8.0


<br>
<br>

# Architecture
<img src="Architecture.png" alt="Alt text" title="PredCaII Method Architecture">

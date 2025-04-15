
# 💳 Credit Card Fraud Detection using Azure ML

This project detects fraudulent credit card transactions using a Random Forest model trained and evaluated through Azure Machine Learning Studio. The dataset used is highly imbalanced, so special attention is given to metrics like precision, recall, and F1 score.

## 📊 Metrics

- **Accuracy**: 99.96%  
- **Precision**: 94.05%  
- **Recall**: 80.61%  
- **F1 Score**: 86.81%  

## 🚀 Tools Used

- Python (pandas, numpy, scikit-learn)
- Azure Machine Learning SDK & Studio
- Python Scripts
  
## 🧠 ML Workflow

1. Data Preprocessing
2. Feature Engineering (Scaling Time and Amount)
3. Model Training (Random Forest Classifier)
4. Evaluation using Accuracy, Precision, Recall, F1 Score
5. Logging Metrics using Azure ML SDK


## 📁 Dataset Info (Important!)

The dataset (data/creditcard.csv) is stored using Git Large File Storage (Git LFS).
To access the actual dataset, you must have Git LFS installed before cloning or pulling the repo.

## 🔧 How to Run

1. Install Git LFS:
   ```bash
   git lfs install

2. Clone the repository:
   ```bash
   git clone https://github.com/BikramAgrawal/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection

3. Pull the dataset file:
   ```bash
   git lfs pull


⚠️ Without Git LFS, you'll only get a small pointer file instead of the actual dataset.


 

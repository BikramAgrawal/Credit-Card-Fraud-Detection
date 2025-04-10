
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

## 📁 Dataset

This project uses the [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle.

> ⚠️ **Note**: Due to GitHub’s 100MB file limit, the dataset is not included in the repository.  
> 📥 Please download the dataset manually and place `creditcard.csv` inside the `data/` folder.

## 🔧 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/BikramAgrawal/Credit-Card-Fraud-Detection.git
   cd Credit-Card-Fraud-Detection

# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from azureml.core import Run
import os

# Get Azure ML run context
run = Run.get_context()

# Load data
data_dir = os.getenv("INPUT_DATA", "./data")
file_path = os.path.join(data_dir, "creditcard.csv")
df = pd.read_csv(file_path)

# Feature scaling
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
df['scaled_time'] = scaler.fit_transform(df[['Time']])
df = df.drop(['Time', 'Amount'], axis=1)

# Features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Log metrics to Azure
run.log("Accuracy", acc)
run.log("Precision", prec)
run.log("Recall", rec)
run.log("F1 Score", f1)
run.complete()

print("Running inside AzureML:", run.id if run else "Not in AzureML")
print(f"Accuracy: {acc}, Precision: {prec}, Recall: {rec}, F1 Score: {f1}")

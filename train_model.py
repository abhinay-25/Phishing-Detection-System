"""
Train all models and save metrics
This script trains multiple ML models and saves the best one
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import pickle
import json
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("🚀 PHISHING URL DETECTION - MODEL TRAINING")
print("=" * 70)

# Load data
print("\n📊 Loading dataset...")
data = pd.read_csv("phishing.csv")
print(f"✅ Dataset loaded: {data.shape[0]} samples, {data.shape[1]} features")

# Prepare data
X = data.drop(['class', 'Index'], axis=1)
y = data['class']

# Convert labels from -1/1 to 0/1 for XGBoost compatibility
y_binary = y.apply(lambda x: 0 if x == -1 else 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)
print(f"📈 Training samples: {X_train.shape[0]}")
print(f"📉 Testing samples: {X_test.shape[0]}")

# Define all models
models = {
    'Gradient Boosting Classifier': GradientBoostingClassifier(random_state=42, n_estimators=100),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Support Vector Machine': SVC(random_state=42, probability=True),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Naive Bayes Classifier': GaussianNB(),
    'Multi-layer Perceptron': MLPClassifier(random_state=42, max_iter=500),
    'XGBoost Classifier': XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss'),
    'CatBoost Classifier': CatBoostClassifier(random_state=42, verbose=0)
}

# Train and evaluate all models
print("\n🔥 Training models...\n")
results = []
best_model = None
best_accuracy = 0

for name, model in models.items():
    print(f"⚙️  Training {name}...")
    
    # Train model
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    
    # Store results
    results.append({
        'model': name,
        'accuracy': round(accuracy, 4),
        'f1_score': round(f1, 4),
        'recall': round(recall, 4),
        'precision': round(precision, 4)
    })
    
    print(f"   ✓ Accuracy: {accuracy:.4f} | F1: {f1:.4f} | Recall: {recall:.4f} | Precision: {precision:.4f}")
    
    # Track best model
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

# Sort results by accuracy
results = sorted(results, key=lambda x: x['accuracy'], reverse=True)

# Save results as JSON
print("\n💾 Saving metrics...")
with open('model_metrics.json', 'w') as f:
    json.dump(results, f, indent=2)
print("✅ Metrics saved to model_metrics.json")

# Save the best model
print(f"\n🏆 Best Model: {best_model_name} (Accuracy: {best_accuracy:.4f})")
print("💾 Saving model...")
with open('pickle/model.pkl', 'wb') as f:
    pickle.dump(best_model, f)
print("✅ Model saved to pickle/model.pkl")

# Display final results
print("\n" + "=" * 70)
print("📊 MODEL COMPARISON RESULTS")
print("=" * 70)
print(f"{'Rank':<6} {'Model':<30} {'Accuracy':<12} {'F1-Score':<12}")
print("-" * 70)
for i, result in enumerate(results, 1):
    emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "
    print(f"{emoji} {i:<4} {result['model']:<30} {result['accuracy']:<12} {result['f1_score']:<12}")
print("=" * 70)

print("\n✨ Training complete! Model is ready to use.")

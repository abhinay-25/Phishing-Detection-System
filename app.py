# Phishing URL Detection - Flask Application
# Modern UI with Metrics Dashboard

from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import warnings
import json
import os
warnings.filterwarnings('ignore')

from feature import FeatureExtraction

app = Flask(__name__)

# Load the trained model
try:
    with open("pickle/model.pkl", "rb") as file:
        model = pickle.load(file)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"⚠️  Warning: Could not load model - {e}")
    model = None

# Load metrics
def load_metrics():
    try:
        with open('model_metrics.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    """Main detection page"""
    if request.method == "POST":
        url = request.form["url"]
        
        try:
            # Extract features
            obj = FeatureExtraction(url)
            features = np.array(obj.getFeaturesList()).reshape(1, 30)
            
            if model:
                # Predict using trained model
                prediction = model.predict(features)[0]
                probability_phishing = model.predict_proba(features)[0, 0]
                probability_safe = model.predict_proba(features)[0, 1]
            else:
                # Fallback to simple rule-based prediction
                probability_safe = simple_predictor(features[0])
                probability_phishing = 1 - probability_safe
            
            return render_template('detect.html', 
                                 xx=round(probability_safe, 2), 
                                 url=url)
        
        except Exception as e:
            print(f"Error processing URL: {e}")
            # Return moderate safety score on error
            return render_template('detect.html', 
                                 xx=0.5, 
                                 url=url)
    
    return render_template("detect.html", xx=-1)

@app.route("/metrics")
def metrics():
    """Metrics dashboard page"""
    metrics_data = load_metrics()
    return render_template("metrics.html", metrics=metrics_data)

@app.route("/api/metrics")
def api_metrics():
    """API endpoint for metrics data"""
    metrics_data = load_metrics()
    return jsonify(metrics_data)

def simple_predictor(features):
    """
    Simple rule-based predictor (fallback when model not available)
    """
    score = 0
    weights = [0.8, 0.5, 0.7, 0.9, 0.6, 0.8, 0.4, 0.9, 0.7, 0.6,
               0.5, 0.7, 0.8, 0.85, 0.75, 0.7, 0.6, 0.8, 0.65, 0.7,
               0.6, 0.6, 0.7, 0.8, 0.8, 0.9, 0.85, 0.75, 0.7, 0.8]
    
    for i, feature in enumerate(features):
        if feature == 1:
            score += weights[i]
        elif feature == -1:
            score -= weights[i]
    
    max_score = sum(weights)
    normalized_score = (score + max_score) / (2 * max_score)
    
    return normalized_score

if __name__ == "__main__":
    print("=" * 70)
    print("🛡️  PHISHING URL DETECTION SYSTEM")
    print("=" * 70)
    print("🌐 Server starting...")
    print("📊 Access the app at: http://127.0.0.1:5000")
    print("📈 View metrics at: http://127.0.0.1:5000/metrics")
    print("=" * 70)
    app.run(debug=True, host='0.0.0.0', port=5000)

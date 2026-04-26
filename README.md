# 🛡️ PhishGuard AI - Advanced Phishing URL Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![ML](https://img.shields.io/badge/Machine%20Learning-97.06%25%20Accuracy-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered phishing URL detection system with a modern, interactive web interface and comprehensive model metrics dashboard. Built with Flask, scikit-learn, XGBoost, and CatBoost.

## ✨ Features

### 🎯 Core Functionality
- **Real-time URL Analysis**: Instant phishing detection with 30+ feature extraction
- **97.06% Accuracy**: Powered by XGBoost machine learning model
- **10 ML Models**: Comprehensive comparison of algorithms
- **Interactive UI**: Modern, responsive design with animated backgrounds
- **Metrics Dashboard**: Visual comparison of all model performances
- **RESTful API**: JSON endpoint for programmatic access

### 🎨 Modern UI Features
- Animated starfield background
- Gradient designs and smooth transitions
- Real-time confidence scoring
- Color-coded risk indicators
- Responsive mobile-friendly layout
- Interactive charts and visualizations

## 📊 Model Performance

| Rank | Model | Accuracy | F1-Score | Recall | Precision |
|------|-------|----------|----------|--------|-----------|
| 🥇 | XGBoost Classifier | 97.06% | 97.39% | 98.30% | 96.50% |
| 🥈 | CatBoost Classifier | 97.01% | 97.35% | 98.14% | 96.57% |
| 🥉 | Random Forest | 96.92% | 97.26% | 97.65% | 96.87% |
| 4 | Multi-layer Perceptron | 96.88% | 97.23% | 98.22% | 96.27% |
| 5 | Decision Tree | 96.02% | 96.43% | 96.11% | 96.74% |
| 6 | Support Vector Machine | 95.12% | 95.70% | 97.33% | 94.13% |
| 7 | Gradient Boosting | 94.93% | 95.50% | 96.19% | 94.81% |
| 8 | K-Nearest Neighbors | 93.98% | 94.63% | 94.98% | 94.29% |
| 9 | Logistic Regression | 93.35% | 94.12% | 95.30% | 92.97% |
| 10 | Naive Bayes | 60.47% | 45.37% | 29.39% | 99.45% |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/vaibhavbichave/Phishing-URL-Detection.git
cd Phishing-URL-Detection
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Train the model** (First time setup)
```bash
python train_model.py
```

4. **Run the application**
```bash
python app_new.py
```

5. **Access the application**
- Main Detector: http://127.0.0.1:5000
- Metrics Dashboard: http://127.0.0.1:5000/metrics
- API Endpoint: http://127.0.0.1:5000/api/metrics

## 📁 Project Structure

```
Phishing-URL-Detection/
├── app_new.py                 # Main Flask application
├── train_model.py             # Model training script
├── feature.py                 # Feature extraction module (30 features)
├── phishing.csv              # Dataset (11,054 samples)
├── model_metrics.json        # Model performance metrics
│
├── pickle/
│   └── model.pkl             # Trained XGBoost model
│
├── templates/
│   ├── detect.html           # Main detection page
│   └── metrics.html          # Metrics dashboard page
│
├── static/
│   ├── detect.css            # Detection page styles
│   └── metrics.css           # Metrics page styles
│
├── requirements.txt          # Python dependencies
└── README_NEW.md            # This file
```

## 🔍 Feature Extraction

The system analyzes **30 different features** from each URL:

### URL-Based Features
1. **UsingIP** - URL uses IP address instead of domain
2. **LongURL** - URL length analysis
3. **ShortURL** - URL shortener detection
4. **Symbol@** - Presence of @ symbol
5. **Redirecting//** - Multiple redirects
6. **PrefixSuffix** - Dash in domain name
7. **SubDomains** - Number of subdomains
8. **HTTPS** - SSL certificate presence
9. **DomainRegLen** - Domain registration length

### Domain-Based Features
10. **Favicon** - Favicon loaded from different domain
11. **NonStdPort** - Non-standard port usage
12. **HTTPSDomainURL** - HTTPS token in domain
13. **AgeofDomain** - Domain age analysis
14. **DNSRecording** - DNS record age

### HTML/JavaScript Features
15. **RequestURL** - External resources ratio
16. **AnchorURL** - Anchor tag analysis
17. **LinksInScriptTags** - Script/link tag patterns
18. **ServerFormHandler** - Form submission analysis
19. **InfoEmail** - Email information patterns
20. **StatusBarCust** - Status bar customization
21. **DisableRightClick** - Right-click disabled
22. **UsingPopupWindow** - Popup window usage
23. **IframeRedirection** - Iframe presence

### External Services
24. **AbnormalURL** - URL abnormality check
25. **WebsiteForwarding** - Redirect count
26. **WebsiteTraffic** - Alexa rank analysis
27. **PageRank** - Google PageRank
28. **GoogleIndex** - Google index status
29. **LinksPointingToPage** - Backlink analysis
30. **StatsReport** - Statistical reports

## 🎨 UI Screenshots

### Main Detection Page
- Clean, modern interface with animated starfield background
- Real-time URL analysis with confidence scoring
- Color-coded results (Green for safe, Red for dangerous)
- Detailed feature analysis breakdown

### Metrics Dashboard
- Trophy card for best performing model
- Interactive comparison table with all models
- Beautiful charts (Bar chart & Radar chart)
- Statistical cards showing key metrics

## 🛠️ Technology Stack

### Backend
- **Flask** - Web framework
- **Python 3.12** - Programming language
- **scikit-learn** - Machine learning library
- **XGBoost** - Gradient boosting framework
- **CatBoost** - Gradient boosting library
- **pandas** - Data manipulation
- **numpy** - Numerical computing

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling (with animations)
- **JavaScript** - Interactivity
- **Chart.js** - Data visualization
- **Font Awesome** - Icons
- **Google Fonts (Poppins)** - Typography

### Feature Extraction
- **BeautifulSoup4** - HTML parsing
- **python-whois** - Domain information
- **requests** - HTTP requests
- **googlesearch-python** - Google search API

## 📈 API Usage

### Get Model Metrics
```bash
curl http://127.0.0.1:5000/api/metrics
```

### Response Format
```json
[
  {
    "model": "XGBoost Classifier",
    "accuracy": 0.9706,
    "f1_score": 0.9739,
    "recall": 0.983,
    "precision": 0.965
  },
  ...
]
```

## 🔄 Retraining the Model

To retrain the model with new data or different parameters:

1. Update the `phishing.csv` dataset
2. Run the training script:
```bash
python train_model.py
```

The script will:
- Load and split the dataset
- Train all 10 models
- Compare performance metrics
- Save the best model to `pickle/model.pkl`
- Generate `model_metrics.json`

## 📊 Dataset Information

- **Source**: Kaggle Phishing Website Dataset
- **Samples**: 11,054 URLs
- **Features**: 30 security indicators
- **Labels**: 
  - `1` = Legitimate (Safe)
  - `-1` = Phishing (Malicious)

## 🚨 Important Notes

### Security Warnings
- This is a machine learning model and may have false positives/negatives
- Always exercise caution when visiting unfamiliar URLs
- Use additional security measures (antivirus, browser protection)

### Performance
- First-time feature extraction may take 5-10 seconds per URL
- Some features require internet connectivity (WHOIS, traffic data)
- Results are probabilistic, not absolute

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Vaibhav Bichave**
- GitHub: [@vaibhavbichave](https://github.com/vaibhavbichave)

## 🙏 Acknowledgments

- Dataset from Kaggle
- Flask and scikit-learn communities
- All contributors and testers

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

## 🎯 Future Enhancements

- [ ] Real-time URL monitoring
- [ ] Browser extension integration
- [ ] API rate limiting
- [ ] User authentication
- [ ] Database for historical analysis
- [ ] Email alert system
- [ ] Mobile app version
- [ ] Deep learning models (CNN, LSTM)

---

**⚠️ Disclaimer**: This tool is for educational and research purposes. Always verify URLs through multiple sources before making security decisions.

**Made with ❤️ and Python**

# 🛡️ Smart Email Security System

An AI-powered Email Security Platform that detects Spam, Phishing Attempts, Suspicious URLs, and Malicious Keywords using Machine Learning and Natural Language Processing (NLP).

## 🚀 Features

### 📧 Spam Detection

* Machine Learning based email classification
* Spam/Ham prediction
* Spam probability score (%)

### 🎣 Phishing Detection

* URL extraction from email content
* Shortened URL detection
* IP-based URL detection
* Suspicious domain identification

### 🔍 Keyword Analysis

* Suspicious keyword highlighting
* Phishing phrase detection
* Risk keyword scoring

### 📊 Security Analytics

* Security score calculation
* Threat level classification
* Spam vs Safe email statistics
* Interactive analytics dashboard

### 🤖 Machine Learning Models

* Random Forest
* Support Vector Machine (SVM)
* Logistic Regression
* Naive Bayes

### 📈 Model Comparison

* Accuracy comparison charts
* Confusion Matrix visualization
* Performance metrics

  * Accuracy
  * Precision
  * Recall
  * F1 Score

### 📑 Reports

* Security analysis reports
* Dataset statistics
* Model performance summary

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Backend

* Flask
* Flask-CORS

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### NLP

* TF-IDF Vectorization
* Text Preprocessing
* Keyword Analysis



---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/harshu-belal/smart-email-security-system.git
cd smart-email-security-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📊 Security Score Formula

```text
Security Score =
100
− (Spam Score × 0.40)
− (Phishing Score × 0.35)
− (Keyword Score × 0.25)
```

---

## 📈 Dataset

Dataset used:

SMS Spam Collection Dataset

Contains:

* Spam messages
* Legitimate (Ham) messages

Used for training and evaluating machine learning models.

---

## 🎯 Future Enhancements

* PDF Report Generation
* Email File Upload (.txt)
* Real-Time Threat Monitoring
* Database Integration
* User Authentication
* Cloud Deployment
* Advanced NLP Models

---

## 👨‍💻 Developer

**Harshit Belal**
B.Tech CSE (AI & ML)

---

## 📜 License

This project is developed for educational and research purposes.

© 2026 Harshit. All Rights Reserved.

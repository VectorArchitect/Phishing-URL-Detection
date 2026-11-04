# 🔐 Phishing URL Detection

A machine learning-based system for detecting potentially malicious URLs using Python, scikit-learn, and Flask.

The project aims to classify URLs as **Phishing** or **Legitimate** by analyzing URL characteristics and applying supervised machine learning algorithms.

> **Project status:** Initial project setup. Dataset preparation, feature extraction, model training, and the Flask application are planned development steps and should be marked complete only after implementation.

## 📌 Overview

Phishing attacks use deceptive URLs to trick users into revealing sensitive information such as passwords, banking credentials, and personal data.

This project focuses on developing an automated detection system that extracts meaningful features from URLs and uses a trained machine learning model to identify potentially malicious links.

## 🎯 Objectives

- Detect potentially malicious and phishing URLs.
- Extract meaningful lexical features from URLs.
- Train and evaluate machine learning classification models.
- Provide predictions through a Flask web application.
- Display prediction results and model outputs through a user-friendly interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas & NumPy | Data processing |
| scikit-learn | Machine learning |
| Matplotlib & Seaborn | Data visualization |
| Flask | Backend and REST API |
| HTML, CSS & JavaScript | Frontend |
| Joblib | Model serialization |

## ⚙️ Planned System Architecture

```text
        User submits URL
               |
               v
        Flask web interface
               |
               v
        URL feature extraction
               |
               v
        Trained ML classifier
               |
               v
        Prediction and score
               |
               v
        Result displayed to user
```

## 🔍 URL Feature Extraction

The system is intended to analyze URL characteristics such as:

- URL length
- Number of dots, hyphens, and digits
- HTTPS scheme presence
- IP-address-based hosts
- Presence of special characters
- Suspicious keywords
- Number of subdomains
- URL-shortening indicators

These are heuristic signals, not definitive proof of malicious intent. HTTPS alone does not establish that a website is trustworthy.

## 🤖 Machine Learning Approach

The project will compare classification algorithms such as:

- Logistic Regression
- Random Forest Classifier
- XGBoost (optional)

Model evaluation will consider:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- ROC-AUC score

Random Forest is the initial candidate model. The final model will be selected based on evaluation results rather than assumed performance.

## 📁 Planned Project Structure

```text
Phishing-URL-Detection/
│
├── app.py
├── feature_extraction.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── dataset/
│   └── phishing_urls.csv
│
├── models/
│   └── phishing_model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── evaluate.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── about.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── tests/
    ├── test_features.py
    └── test_api.py
```

*This is a proposed structure; files and directories will be added as the project is implemented.*

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later (use a version supported by the selected dependencies)
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/VectorArchitect/Phishing-URL-Detection.git
cd Phishing-URL-Detection
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Once `requirements.txt` has been added:

```bash
pip install -r requirements.txt
```

### 4. Run the application

Once the Flask application and trained model are implemented:

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

> The application is not runnable until its dependencies, dataset pipeline, trained model, and Flask entry point have been implemented.

## 📊 Evaluation

Evaluation results, dataset details, and model comparisons will be documented here after experiments are completed. No performance figures are claimed at this stage.

## 🔮 Development Roadmap

- [ ] Select and document a suitably licensed phishing URL dataset.
- [ ] Implement data cleaning and preprocessing.
- [ ] Build and test URL feature extraction.
- [ ] Train and compare classification models.
- [ ] Evaluate generalization on unseen domains.
- [ ] Integrate the selected model with a Flask API.
- [ ] Build an interactive dashboard.
- [ ] Add explainability for individual predictions.
- [ ] Add scan history and downloadable reports.
- [ ] Add automated tests and usage documentation.

## ⚠️ Security Notes & Disclaimer

This project is intended for educational and research purposes. Its predictions are not a guarantee that a URL is safe or malicious.

- A URL classified as legitimate may still be malicious.
- Model confidence is not a verified probability of real-world safety.
- The initial design analyzes URL strings and should not automatically visit submitted URLs.
- Treat submitted URLs and datasets as untrusted input.
- Review dataset licensing and attribution requirements before redistribution.

## 👨‍💻 Author

**Savinav Sharma**

- GitHub: [@VectorArchitect](https://github.com/VectorArchitect)

---

If you find this project interesting, consider giving the repository a star!

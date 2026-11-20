# Phishing URL Detection System

A Python-based machine learning project for identifying potentially malicious URLs through hybrid feature extraction, ensemble classification, and a Flask web interface/API.

> **Repository status:** This repository currently contains project documentation and configuration files. The application source code, dataset, trained models, and frontend assets have not yet been pushed. The sections below describe the system documented for this project; setup commands will become executable once the corresponding files are added.

## Overview

Phishing URLs imitate legitimate websites or use deceptive structures to persuade people to disclose credentials and other sensitive information. This project explores the use of machine learning to classify URLs as **potentially phishing** or **potentially legitimate**.

The documented system combines URL lexical analysis, domain-related attributes, and SSL/security indicators. Extracted features are supplied to trained classifiers, with predictions exposed through a Flask application.

This is a defensive educational/research project. A model prediction is an indicator, not a guarantee that a website is safe or malicious.

## Documented capabilities

- Hybrid URL feature extraction.
- Comparison of ensemble machine learning classifiers.
- Flask-based web interface and REST API.
- Single-URL and batch prediction workflows.
- Prediction scores and model evaluation visualizations.
- Feature-importance information for model interpretation.

These capabilities are described in the project documentation; they should not be considered runnable from this repository until the implementation is uploaded.

## System design

```text
             URL submitted by user
                      |
                      v
              Flask interface/API
                      |
                      v
             URL feature extraction
                      |
                      v
             Hybrid feature vector
                      |
                      v
              Trained classifier
                      |
                      v
          Phishing / Legitimate result
                      |
                      v
              Result and score
```

## Feature engineering

The project documentation describes **29 hybrid features** across three groups:

| Feature group | Count | Examples |
|---|---:|---|
| Lexical | 20 | URL length, special characters, suspicious keywords, IP-address indicators |
| Domain | 6 | Subdomain count, domain-related attributes, entropy |
| SSL/security | 3 | HTTPS and certificate-related indicators |
| **Total** | **29** | |

Some domain attributes may require external lookups. A feature based on a mock or unavailable lookup must be identified as such and must not be presented as verified threat intelligence.

## Machine learning

The documented model comparison includes:

- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM

The project documentation identifies **XGBoost** as the selected model.

### Reported evaluation results

| Metric | Documented result |
|---|---:|
| Accuracy | 97.40% |
| Precision | 97.20% |
| Recall | 97.60% |
| F1-score | 97.40% |
| ROC-AUC | 99.72% |

These are figures reported in the project's documentation, not independently reproduced or verified from the contents of this GitHub repository. Performance depends on dataset provenance, class balance, preprocessing, train/test separation, and evaluation methodology. In particular, URL datasets should be split carefully to reduce domain or near-duplicate leakage.

## Technology stack

The documented implementation uses or evaluates:

| Area | Technologies |
|---|---|
| Language | Python |
| Data processing | Pandas, NumPy |
| Machine learning | scikit-learn |
| Boosting | XGBoost, LightGBM |
| Backend/API | Flask |
| URL/domain analysis | URL parsing and domain extraction utilities |
| Visualization | Matplotlib, Seaborn |
| Model persistence | Pickle / Joblib, as applicable to the implementation |

The final dependency list and exact versions will be recorded in `requirements.txt` when the source code is added.

## Planned repository layout

The actual layout may differ as the source is uploaded. A maintainable target structure is:

```text
Phishing-URL-Detection/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── app/                 # Flask routes and application entry point
├── src/                 # Feature extraction and preprocessing
├── training/            # Training and evaluation scripts
├── tests/               # Unit and API tests
├── templates/           # Web interface templates
├── static/              # CSS, JavaScript and public assets
├── docs/                # Project and API documentation
├── data/                # Local datasets (not committed by default)
└── models/              # Local trained artifacts (not committed by default)
```

## Installation and execution

The following is the intended local workflow. **It is not yet executable from this repository** because the application entry point and dependency manifest have not been uploaded.

### 1. Clone the repository

```bash
git clone https://github.com/VectorArchitect/Phishing-URL-Detection.git
cd Phishing-URL-Detection
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

After `requirements.txt` is added:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

The final run command will be documented after the actual Flask entry point and model-loading workflow are present. Do not assume an `app.py` or `api_server.py` filename until it is confirmed in the source tree.

## API

The project documentation describes single-URL prediction and batch-prediction workflows. Exact endpoint paths, request schemas, response fields, and error codes will be documented from the implemented Flask routes once those files are committed.

## Dataset and model files

Datasets and trained model artifacts are intentionally excluded from version control by default.

Before publishing or redistributing any dataset or model, verify:
- its original source and license;
- whether redistribution is permitted;
- whether personal or sensitive data is present;
- how the artifact was generated and evaluated.

Provide reproducible download or preparation instructions where possible. Do not commit secrets, private datasets, or large generated artifacts.

## Security and responsible use

- Do not automatically open or browse URLs submitted for classification.
- Treat URLs, datasets, and request bodies as untrusted input.
- Do not enter real credentials into suspicious websites during testing.
- HTTPS does not by itself prove that a website is trustworthy.
- A legitimate prediction can be a false negative; a phishing prediction can be a false positive.
- Do not use model confidence as a guarantee of real-world safety.
- Use the project only for authorized defensive, educational, and research purposes.

## Development roadmap

- [ ] Publish the application source code and dependency manifest.
- [ ] Document dataset provenance, license, and preparation.
- [ ] Add reproducible training and evaluation scripts.
- [ ] Add automated feature-extraction and API tests.
- [ ] Document exact API request/response schemas.
- [ ] Add setup instructions verified in a clean environment.
- [ ] Add screenshots of the actual web interface.
- [ ] Document model limitations and evaluation methodology.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

**Savinav Sharma**  
GitHub: [@VectorArchitect](https://github.com/VectorArchitect)

---

If you find this project useful, consider starring the repository.

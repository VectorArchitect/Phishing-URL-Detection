# Phishing URL Detection System

A Python project exploring phishing URL detection through URL feature extraction, machine-learning classification, and a Flask API with a React interface prototype.

> **Status: work in progress.** The supplied archive contains source prototypes and documentation, but not a complete runnable system. The training/data-pipeline module, training script, dataset, trained model artifacts, and automated tests are absent. The Flask API imports a missing `data_pipeline` module and expects model files that are not present.

## Repository contents

| Area | Included | Current status |
|---|---|---|
| Feature extraction | `feature_extraction.py` | Present; includes a mock domain-age value |
| Flask API | `api_server.py` in the supplied archive | Depends on missing pipeline and model artifacts |
| Frontend | React/TypeScript UI prototype | Prediction currently uses local heuristic logic; API fetch is commented out |
| Configuration | YAML config | Present |
| Dependencies | Python requirements | Present |
| Documentation | SRS, user manual, deployment guide, model notes, checklist | Supplied |
| Dataset / training pipeline | Dataset, `data_pipeline.py`, training script | Not supplied |
| Model artifacts | Model, scaler/pipeline, metadata | Not supplied |
| Tests / CI | Automated tests and workflows | Not supplied |

## Important implementation notes

- The domain-age feature is explicitly hash-based mock data, not WHOIS registration intelligence.
- SSL checks perform network connections and can fail due to DNS, connectivity, certificate, or timeout conditions.
- Feature names/count/order must be reconciled and frozen between training and inference before predictions can be trusted.
- The model documentation reports 97.40% accuracy, 97.20% precision, 97.60% recall, 0.974 F1, and 0.9972 ROC-AUC. The dataset, training code, model, and evaluation outputs were not supplied, so these figures are documented claims and are not independently reproducible from this repository.
- The frontend currently demonstrates heuristic scoring, not predictions from the trained ML model.

## Setup

Python 3.8+ is the documented baseline.

```bash
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r 07_Deployment/requirements.txt
```

This only prepares the Python environment. The current source set is not yet sufficient to launch a working prediction service because the pipeline module and trained model artifacts are missing.

## API routes documented in the Flask source

| Method | Route | Purpose |
|---|---|---|
| GET | `/` | Browser interface |
| GET | `/health` | Health/model status |
| POST | `/predict` | Single URL prediction |
| POST | `/batch_predict` | Batch URL prediction |

These are source-level routes; they have not been verified end-to-end.

## Security and data handling

- Treat model output as a risk signal, not proof that a site is safe or malicious.
- Do not visit suspicious URLs for testing; use synthetic strings or isolated, authorized test environments.
- Do not commit private datasets, credentials, `.env` files, virtual environments, logs, or generated model binaries.
- Only load pickle/joblib artifacts from trusted sources.
- Verify dataset provenance, licensing, class balance, leakage risks, and train/test separation before publishing performance claims.

## Roadmap

1. Implement and document dataset ingestion and cleaning.
2. Add the missing data pipeline and model-training/evaluation scripts.
3. Reconcile feature count, names, ordering, and preprocessing across training and inference.
4. Replace or disable mock domain-age values.
5. Add a small license-compatible fixture and automated unit/API tests.
6. Connect the frontend to the Flask API and show unavailable-service states.
7. Add reproducible evaluation outputs and CI checks.
8. Add deployment assets after a clean installation and end-to-end run succeed.

## Documentation

Project documentation and reference material belong under `01_Documentation/`; deployment notes and dependencies are under `07_Deployment/`. Model notes are under `05_Models/`.

## License

MIT License. See [LICENSE](LICENSE).

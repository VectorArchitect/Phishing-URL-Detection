# Model Artifacts

This directory is reserved for trained model files and their metadata. No model binaries or training pipeline were present in the supplied project archive, so none are committed.

The supplied project notes describe XGBoost as the selected model and report the following test metrics:

| Metric | Reported value |
|---|---:|
| Accuracy | 97.40% |
| Precision | 97.20% |
| Recall | 97.60% |
| F1-score | 0.974 |
| ROC-AUC | 0.9972 |

**These are documented claims, not independently verified results.** The dataset, training script, evaluation outputs, and serialized model were not supplied.

The notes describe a 29-feature schema (20 lexical, 6 domain, 3 SSL/security), but the supplied feature extractor's schema must be programmatically counted and reconciled with the model before training/inference can be considered compatible.

Expected artifacts mentioned by the project documentation:

- `best_model.pkl`
- `pipeline.pkl`
- `feature_names.json`
- `model_metadata.json`

Do not add these files until they are generated from a documented, reproducible training run. Model binaries are ignored by Git; publish them through a trusted release or artifact store if appropriate.

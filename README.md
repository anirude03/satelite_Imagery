# Satellite Imagery–Based Multimodal Property Valuation
  # Project Overview

This project develops a multimodal regression system to predict residential property prices by combining:

Structured tabular housing data (size, quality, neighborhood metrics, grade, condition, Property Age, Renovation Period)

Satellite imagery capturing environmental and spatial context (Greenery, Roads, Waterfront, Clustering)

Unlike traditional valuation models that rely only on numerical attributes, this system integrates visual features such as green cover, road connectivity, and neighborhood layout, leading to improved predictive performance and better interpretability.


 # Key Features

Multimodal learning (Tabular + Images)

ResNet-18 backbone for efficient image encoding

Early fusion architecture

Log-price regression

Grad-CAM–based explainability

Modular and reproducible codebase

# Repository Structure
```

├── train(1).csv
├── test(2).csv
│
├── map_images/
│   ├── train/
│   └── test/
│
├── preprocessing.ipynb
│
├── baseline_models_and_GRAD-CAM.ipynb
│   ├── Baseline Models
│   ├── Multimodal Architecture
│   ├── CNN + XGBoost Model
│   ├── Test Prediction
│   └── Grad-CAM and Overlays
│
├── model_training.ipynb
│
├── image_fetcher.py              # Script to fetch satellite imagery
│
├── best_multimodal_model.pt      # Trained multimodal model weights
├── _predictions.csv              # Test set predictions
│
├── gradcam/
│   └── (saved Grad-CAM visualizations)
│
├── tabular_preprocessed.joblib  # Saved tabular preprocessing artifacts
├── train_config.json            # Training configuration and hyperparameters
│
├── requirements.txt
└── README.md
```

#  Satellite Imagery–Based Multimodal Property Valuation

---

##  Installation & Setup

### Install Dependencies

Install all required Python packages using:

```bash
pip install -r requirements.txt

Download satellite imagery using lat,long coordinates:
python image_fetcher.py


# How to Run

# Preprocessing & EDA
preprocessing.ipynb



# Baseline Models
baseline_models_and_GRAD-CAM.ipynb  —  Baseline Models

This section includes:

Tabular-only baseline models

Multimodal Architecture Code

Performance benchmarking
    

# Model Training
model_training.ipynb
   
Run this notebook to:

Train the multimodal model

Run multiple epochs

Fine-tune or load the already trained model (best_multimodal_model.pt)
   
# Test Prediction and Explanability
baseline_models_and_GRAD-CAM.ipynb  
— Multimodal Architecture  
— CNN + XGBoost Model  
— Test Prediction  
— Grad-CAM and Overlays

This section covers:

Multimodal inference on the test dataset

Generation of test predictions

Grad-CAM explainability and overlays


# Outputs
final_predictions.csv        — Test set predictions
best_multimodal_model.pt     — Trained multimodal model weights
outputs/gradcam/             — Explainability visualizations


Author

Anirudh Kumar Verma
Multimodal Machine Learning | Computer Vision | Data Science

License

This project is for academic and research purposes.





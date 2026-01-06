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

├──── train(1).csv
├── test(2).csv
│
├── map_images/
│   ├── train/
│   └── test/
│
├── preprocessing.ipynb
|
├── baseline_models_and_GRAD-CAM.ipynb
|     -- Baseline Models
|     -- Multimodal Architecture
|     -- CNN + XGboost Model
|     -- Test Prediction
|     -- GRAD-CAM and Overlays
|    
├── model_training.ipynb
├
├── image_fetcher.py       # to fetch the satelite Imagery
|
|── best_multimodal_model.pt
├── final_predictions.csv
├── gradcam/
|── tabular_preprocessed.joblib
|── train_config.json
|
├── requirements.txt
└── README.md

# Installation & Setup

 # Install dependencies
     -- requirements.txt

 # Fetch satellite images
   -- image_fetcher.py

# How to Run

  # Preprocessing & EDA
    preprocessing.ipynb

# Baseline Models
   baseline_models_and_GRAD-CAM.ipynb
      --- Baseline Models     

# Model Training
   model_training.ipynb     # Run Epochs to train the model or use the already trained model (best_multimodel.pt) and fine tune.

# Test Prediction and Explanability
   basline_models_and_GRAD-CAM.ipynb
      -- Multimodal Architecture
      -- CNN + XGboost Model
      -- Test Prediction
|     -- GRAD-CAM and Overlays 


# Outputs
final_predictions.csv — Test set predictions

best_multimodal_model.pt — Trained model weights

outputs/gradcam/ — Explainability visualizations


Author

Anirudh Kumar Verma
Multimodal Machine Learning | Computer Vision | Data Science

License

This project is for academic and research purposes.





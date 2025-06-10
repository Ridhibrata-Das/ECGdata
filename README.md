# Multi-Modal Cardiac Arrhythmia Prediction System

This project aims to develop an advanced system that combines ECG, PPG (photoplethysmography), and ballistocardiography signals to predict cardiac arrhythmias 24-48 hours before onset.

## Project Structure

- `datasets/`: Will contain datasets (e.g., PTB-XL, MIT-BIH Arrhythmia, PhysioNet Challenge 2015, Multi-Pathology BCG). Awaits zipped dataset.
- `src/`: Contains all source code.
  - `data_preprocessing/`: Scripts for signal synchronization and artifact removal.
  - `feature_engineering/`: Scripts for extracting features from different modalities.
  - `models/`: Implementation of deep learning models, including feature extractors and the attention fusion mechanism.
  - `pipelines/`: Training and prediction pipelines.
  - `utils/`: Utility functions for normalization, explainability, etc.
- `tests/`: Unit tests for the project.
- `requirements.txt`: Python package dependencies.

## System Architecture Overview

The system will use a multi-modal fusion framework with an attention mechanism to combine information from ECG, PPG, and BCG signals. Key components include:
- Signal-specific feature extractors (e.g., 1D ResNet for ECG, TCN for PPG).
- Cross-modal attention (e.g., Transformer-based).
- Temporal analysis for pattern recognition (e.g., Dilated Causal Convolutions).

## Implementation Details

Refer to the issue statement for a detailed breakdown of:
- Data preprocessing steps.
- Feature engineering specifics for each modality.
- Model training strategy.
- Validation protocol.

## Tools & Libraries
- Signal Processing: BioSPPy, HeartPy, WFDB
- Deep Learning: PyTorch, PyTorch Lightning, MONAI
- Explainability: Captum

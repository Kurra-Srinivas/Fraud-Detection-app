![Fraud Detection App](https://github.com/Kurra-Srinivas/Fraud-Detection-app/blob/main/Fraud%20Detection%20App%20image.png)
# Fraud Detection Project (Using ML and Deployed using streamlit)

This project implements a machine learning-based fraud detection system for financial transactions. It includes a Jupyter notebook for exploratory data analysis (EDA) and model training, a Streamlit web application for interactive fraud predictions, and a dataset (https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset/data). The model leverages logistic regression with balanced class weights to address the imbalanced nature of fraud data, achieving high recall for detecting fraudulent transactions.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The Fraud Detection Project aims to identify fraudulent financial transactions using machine learning. The Jupyter notebook (`notebooks/Analysis_Model.ipynb`) performs EDA, data preprocessing, and trains a logistic regression model to classify transactions as fraudulent or non-fraudulent. The Streamlit app (`src/app.py`) provides a user-friendly interface to input transaction details and receive real-time fraud predictions.

Key features:
- Analysis of transaction data with features like `step`, `type`, `amount`, and `isFraud`.
- Logistic regression model with balanced class weights to handle imbalanced data (0.13% fraud rate).
- Interactive web app for fraud prediction.

## Dataset
The dataset (`data/AIML Dataset.csv`) contains 6,362,620 financial transaction records with the following key columns:
- `step`: Time step of the transaction.
- `type`: Transaction type (e.g., PAYMENT, TRANSFER, CASH_OUT).
- `amount`: Transaction amount.
- `oldbalanceOrg`, `newbalanceOrig`: Origin account balances before and after the transaction.
- `oldbalanceDest`, `newbalanceDest`: Destination account balances before and after the transaction.
- `isFraud`: Binary label (1 for fraudulent, 0 for non-fraudulent).

**Note**: If the dataset exceeds GitHub's 100 MB limit, it is hosted externally. Download it from [Insert External Link, e.g., Google Drive or Kaggle] and place it in the `data/` folder.

## Repository Structure
```
fraud-detection-project/
├── data/
│   └── AIML Dataset.csv
├── notebooks/
│   └── Analysis_Model.ipynb
├── src/
│   └── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

- `data/`: Contains the dataset (`AIML Dataset.csv`).
- `notebooks/`: Includes the Jupyter notebook for EDA and model training.
- `src/`: Holds the Streamlit app code (`app.py`).
- `requirements.txt`: Lists Python dependencies.
- `README.md`: Project documentation.
- `LICENSE`: MIT License file.
- `.gitignore`: Excludes unnecessary files (e.g., virtual environments).

### Deployed Streamlit App
The app is deployed on Streamlit Community Cloud. Access it at https://fraud-detection-app-taqhypmjn8savxewsib3yw.streamlit.app/.

## Model Details
- **Algorithm**: Logistic Regression with `class_weight='balanced'` to handle the imbalanced dataset (0.13% fraud cases).
- **Features**: `step`, `type` (one-hot encoded), `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`.
- **Preprocessing**:
  - Numerical features scaled using `StandardScaler`.
  - Categorical feature `type` encoded using `OneHotEncoder`.
- **Performance** (on test set):
  - Accuracy: 94.67%
  - Fraud class (isFraud=1):
    - Precision: 0.02 (low due to imbalance)
    - Recall: 0.94 (high, good at detecting fraud)
    - F1-Score: 0.04
  - See `notebooks/Analysis_Model.ipynb` for detailed metrics and confusion matrix.

**Limitations**:
- Low precision for fraud due to class imbalance.
- Future improvements: Use SMOTE for oversampling, test ensemble models (e.g., Random Forest, XGBoost), or tune hyperparameters.

### 📫 How to Reach Me
- 📧 Email:(srinivaskurra886@gmail.com)
- 📧 Linkedin:(https://www.linkedin.com/in/kurra-srinivas-31727420b/)
- 📸 Instagram:(https://www.instagram.com/_srinivas.kurra/profilecard/?igsh=MWxuNnNpNXc2anhhMg==)



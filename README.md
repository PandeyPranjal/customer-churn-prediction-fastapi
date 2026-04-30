🚀 Customer Churn Prediction System (FastAPI + Streamlit)
📌 Overview

This project is a production-style Machine Learning system that predicts whether a telecom customer is likely to churn.
It integrates a trained ML model with a FastAPI backend for real-time inference and a Streamlit frontend for interactive usage.

⚡ Features
🔍 Real-time churn prediction via REST API
🧠 Machine Learning model (Random Forest)
⚖️ Class imbalance handled using SMOTE
🧾 Structured input validation using Pydantic
🌐 Interactive UI with Streamlit
📊 End-to-end pipeline: Input → Preprocessing → Model → Prediction
🏗️ System Architecture
User Input (Streamlit UI)
        ↓
FastAPI Backend (/predict endpoint)
        ↓
Data Preprocessing + Encoding
        ↓
Trained ML Model (Random Forest)
        ↓
Prediction Output (Churn / No Churn + Probability)
🛠️ Tech Stack
Python
FastAPI
Streamlit
Scikit-learn
Pandas, NumPy
Imbalanced-learn (SMOTE)
📊 Model Details
Algorithm: Random Forest Classifier
Dataset: Telco Customer Churn
Accuracy: ~85%
Preprocessing:
Label Encoding for categorical variables
Handling missing values
Feature alignment during inference
🌐 Live Demo
🔗 API (Swagger UI): [Add your Render link here]
🔗 Streamlit App: [Add your Streamlit link here]
📂 Project Structure
customer-churn-fastapi-ml/
│
├── app/                # FastAPI backend
│   ├── main.py
│   ├── predict.py
│   ├── schema.py
│
├── model/              # Saved model & encoders
│   ├── customer_churn_model.pkl
│   ├── encoders.pkl
│
├── notebook/           # Training & analysis
│   └── churn_analysis.ipynb
│
├── streamlit_app.py    # Frontend UI
├── requirements.txt
├── README.md
▶️ How to Run Locally
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/customer-churn-predition-fastapi.git
cd customer-churn-fastapi-ml
2. Install dependencies
pip install -r requirements.txt
3. Run FastAPI server
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs
4. Run Streamlit app
streamlit run streamlit_app.py
🧠 Key Learnings
Building REST APIs for ML models using FastAPI
Handling feature consistency between training and inference
Managing class imbalance using SMOTE
Deploying ML systems for real-world usage
📌 Future Improvements
Docker containerization
CI/CD pipeline integration
Model monitoring & logging
Use of advanced feature engineering
👨‍💻 Author

PandeyPranjal
🔗 https://github.com/pandeypranjal

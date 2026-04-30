# 🚀 Customer Churn Prediction System (FastAPI + Streamlit)

## 📌 Overview

This project is a **production-oriented Machine Learning system** that predicts whether a telecom customer will churn.
It integrates a trained model with a **FastAPI backend for real-time inference** and a **Streamlit frontend for interactive usage**.

Unlike basic ML projects, this system focuses on **deployment, API design, and real-world usability**.

---

## ⚡ Key Features

* 🔍 Real-time churn prediction via REST API
* 🧠 Random Forest model trained on Telco dataset
* ⚖️ Class imbalance handled using SMOTE
* 🧾 Input validation using Pydantic
* 🌐 Interactive UI with Streamlit
* 📊 End-to-end pipeline from input to prediction

---

## 🏗️ System Architecture

```
User Input (Streamlit UI)
        ↓
FastAPI Backend (/predict)
        ↓
Data Preprocessing (Encoding + Feature Alignment)
        ↓
Machine Learning Model (Random Forest)
        ↓
Prediction Output (Churn + Probability)
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas, NumPy
* Imbalanced-learn (SMOTE)

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Dataset: Telco Customer Churn
* Accuracy: ~85%
* Preprocessing:

  * Label Encoding
  * Handling missing values
  * Feature alignment during inference

---

## 🌐 Live Demo

* 🔗 API (Swagger UI): https://customer-churn-prediction-rd7z.onrender.com/docs
* 🔗 Streamlit App: https://customer-churn-prediction-built-by-pranjal.streamlit.app/

---

## 📂 Project Structure

```
customer-churn-prediction-fastapi/
│
├── app/
│   ├── main.py
│   ├── predict.py
│   ├── schema.py
│   └── __init__.py
│
├── model/
│   ├── customer_churn_model.pkl
│   ├── encoders.pkl
│
├── notebook/
│   └── churn_analysis.ipynb
│
├── streamlit_app.py
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/PandeyPranjal/customer-churn-prediction-fastapi.git
cd customer-churn-prediction-fastapi
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run FastAPI server

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 4. Run Streamlit UI

```
streamlit run streamlit_app.py
```

---

## 🧠 Key Learnings

* Building ML inference APIs using FastAPI
* Handling feature consistency between training and inference
* Managing class imbalance using SMOTE
* Designing end-to-end ML systems

---

## 📌 Future Improvements

* Docker containerization
* CI/CD pipeline integration
* Model monitoring & logging
* Replace LabelEncoder with robust pipelines

---

## 👨‍💻 Author

**PandeyPranjal**


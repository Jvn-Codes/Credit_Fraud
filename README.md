# 💳 Credit Card Fraud Detection

A machine learning-based web application that detects fraudulent credit card transactions using behavioral patterns.

## 🌐 Live Demo
👉 https://jvn-codes-credit-fraud.streamlit.app/

---

## 🚀 Features
- Predicts fraud probability in real-time  
- Simple and interactive web interface  
- User-friendly inputs (no technical knowledge required)  
- Built using transaction behavior data  

---

## 🧠 How It Works
The model analyzes transaction patterns such as:
- Distance from home  
- Purchase amount vs usual spending  
- Online vs offline transaction  
- Chip and PIN usage  

It then predicts the **probability of fraud** using a trained machine learning model.

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 🤖 Model
- Algorithm: Random Forest Classifier  
- Handles imbalanced data  
- Outputs probability instead of just classification  

---

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py

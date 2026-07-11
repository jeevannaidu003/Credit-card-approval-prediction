# 💳 CreditWise AI – Credit Card Approval Prediction using Machine Learning

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask">

<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn">

<img src="https://img.shields.io/badge/XGBoost-Gradient%20Boosting-green?style=for-the-badge">

<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge">

</p>

---

# 📌 Project Overview

**CreditWise AI** is an intelligent Credit Card Approval Prediction System developed using Machine Learning and Flask.

The application predicts whether a customer is likely to receive credit card approval based on demographic, employment, income, and financial information.

The project combines:

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Model Comparison
- Flask Backend
- Modern Responsive UI

into one complete end-to-end application.

---

# 🚀 Live Demo

🌐 **Website**

https://credit-card-approval-prediction-ym35.onrender.com

---

# 📸 Project Preview

## Home Page

> Add screenshot here

```
images/home.png
```

---

## Prediction Page

> Add screenshot here

```
images/predict.png
```

---

## Result Page

> Add screenshot here

```
images/result.png
```

---

# ✨ Features

✅ Credit Card Approval Prediction

✅ Premium Responsive UI

✅ Machine Learning Integration

✅ Random Forest Prediction

✅ Confidence Score

✅ Risk Level Detection

✅ AI Recommendation

✅ Feature Engineering

✅ Label Encoding

✅ Model Comparison

✅ Flask Web Application

✅ Deployment Ready

---

# 📊 Dataset

The project uses two datasets:

- Application Record Dataset
- Credit Record Dataset

After preprocessing they are merged into one dataset used for model training.

### Final Dataset

- **Rows:** 36,457
- **Columns:** 18
- **Target Variable:** TARGET

---

# 🧠 Machine Learning Models

The following algorithms were trained and evaluated.

| Model | Status |
|--------|---------|
| Logistic Regression | ✅ |
| Decision Tree | ✅ |
| Random Forest | ⭐ Best Model |
| XGBoost | ✅ |

The Random Forest classifier achieved the best overall performance and was selected for deployment.

---

# ⚙️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- XGBoost
- Joblib

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### Deployment

- Render

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
Credit Card Approval Prediction/

│

├── dataset/

│      application_record.csv

│      credit_record.csv

│      final_credit_card_dataset.csv

│

├── src/

│      data_preprocessing.py

│      dataset_analysis.py

│      logistic_regression.py

│      decision_tree.py

│      random_forest.py

│      xgboost_model.py

│      model_comparison.py

│

├── saved_models/

│      best_model.pkl

│      feature_columns.pkl

│

│      encoders/

│

├── templates/

│      index.html

│      result.html

│

├── static/

│      css/

│

│      js/

│

├── app.py

├── requirements.txt

└── README.md
```

---

# ⚡ Workflow

```text
Raw Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Encoding

↓

Model Training

↓

Model Evaluation

↓

Best Model Selection

↓

Flask Integration

↓

Prediction

↓

Deployment
```

---

# 📈 Prediction Features

The model uses:

- Gender
- Car Ownership
- Property Ownership
- Number of Children
- Annual Income
- Income Type
- Education Level
- Family Status
- Housing Type
- Occupation
- Family Members
- Work Phone
- Phone
- Email
- Age
- Employment Years

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/jeevannaidu003/credit-card-approval-prediction.git
```

Move into the project

```bash
cd credit-card-approval-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📊 Results

The deployed model predicts whether a customer is likely to receive credit card approval based on the provided information.

The application also provides:

- Prediction Confidence
- Risk Level
- AI Recommendation

---

# 🔮 Future Improvements

- Deep Learning Model
- Explainable AI (SHAP)
- User Authentication
- Dashboard Analytics
- Database Integration
- REST API
- Docker Support
- Cloud Deployment

---

# ⚠️ Disclaimer

This application is developed for **educational and portfolio purposes only**.

Predictions are generated by a machine learning model and should **not** be used as actual banking or financial approval decisions.

---

# 👨‍💻 Author

## Jeevan Naidu Vattikunta

Final Year B.Tech (AI & ML)

Sri Venkateswara College of Engineering

### Connect with me

GitHub

https://github.com/jeevannaidu003

LinkedIn

https://www.linkedin.com/in/jeevan-naidu-vattikunta-047125296

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.

It motivates me to build more AI and Machine Learning projects.

---

<p align="center">

Made with ❤️ using Python, Flask and Machine Learning

</p>

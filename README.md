# 🏠 House Price Prediction Web App

This is a Flask-based web application that predicts house prices using a **Linear Regression** model. The app takes user inputs like location, number of bedrooms (BHK), bathrooms, square footage, etc., and returns an estimated house price.

---

## 📌 Features

- 🔧 Built with **Flask** (Python web framework)
- 📥 User inputs:
  - Location
  - BHK (Number of Bedrooms)
  - Bath (Number of Bathrooms)
  - Balcony (Bedrooms)
  - Sqft (Area in Square Feet)
  - Area Type
  - Availability
- 🤖 Predicts house prices using a trained **Linear Regression model**
- 🎨 Fully styled and responsive frontend using **HTML and CSS**
- 💡 Clean, beginner-friendly codebase with proper structure

---

## 🧠 Machine Learning Model

- **Model Used**: Linear Regression
- **Dataset**: Open-source housing dataset (Bengaluru House Data)
- **Features Used**: 
  - Numerical: `bhk`, `bathroom`, `bedroom`, `total_sqft`
  - Categorical (One-Hot Encoded): `location`, `area_type`, `availability`

The model was trained using preprocessed features and serialized using `pickle` for use in the Flask app.

---

## 🗂 Project Structure
├── app.py # Flask backend
├── model.pkl # Trained Linear Regression model
├── X_columns.pkl # One-hot encoded column names
├── templates/
│ └── index.html # Frontend form and results display
└── README.md # Documentation


---

## 🚀 How to Run the App

### ✅ Prerequisites

- Python 3.x
- pip

### ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Moreaniket/House-Price-Prediction.git
cd House-Price-Prediction
python -m venv venv
venv\Scripts\activate        
pip install flask numpy scikit-learn
python app.py
http://127.0.0.1:5000



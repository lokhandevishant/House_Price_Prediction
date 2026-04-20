# 🏡 House Price Prediction System

A production-level machine learning application that predicts housing prices based on the [Yasserh Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset). This project transitions a research-oriented Jupyter Notebook into a modular, scalable architecture using **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 🏗️ Project Architecture

The project follows a modular design to ensure separation of concerns, making it easier to maintain and scale:

* **`app/processor.py`**: Centralized data engineering pipeline for cleaning, handling outliers, and feature encoding.
* **`app/model.py`**: Encapsulates model training logic, performance evaluation ($R^2$ and MSE), and inference.
* **`app/main.py`**: RESTful API built with FastAPI that provides endpoints for model training and real-time predictions.
* **`ui/app.py`**: An interactive web interface built with Streamlit for user-friendly price estimation.

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### 2. Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Running the Application

To run the full system, you need to start the backend and frontend in separate terminals:

#### ▶️ Step A: Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

* API available at: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs

---

#### ▶️ Step B: Start the Streamlit UI

```bash
streamlit run ui/app.py
```

* UI available at: http://localhost:8501

---

## 🛠️ API Endpoints

### `POST /train`

* Retrains the model using the dataset in `/data`
* Saves the updated model to `/models/model.pkl`

### `POST /predict`

* Accepts a JSON payload of house features
* Returns the estimated house price

---

## 📊 Model Performance

* **Algorithm**: Multiple Linear Regression

* **Key Features**:

  * Area
  * Bedrooms
  * Bathrooms
  * Stories
  * Air Conditioning
  * Parking

* **Baseline Accuracy**:

  * ~$65%$ $R^2$ Score

---

## 📂 Directory Structure

```
House_Price_Prediction/
├── app/
│   ├── main.py
│   ├── processor.py
│   └── model.py
├── data/
│   └── housing.csv
├── models/
│   └── model.pkl
├── ui/
│   └── app.py
└── requirements.txt
```

---

## 📈 Future Improvements

To improve the baseline $R^2$ score beyond 65%, the following enhancements are planned:

* **Outlier Removal**
  Implement Interquartile Range (IQR) filtering for `price` and `area`.

* **Feature Scaling**
  Use `StandardScaler` to normalize numerical features.

* **Advanced Algorithms**
  Explore non-linear models such as:

  * Random Forest
  * XGBoost

---

## 💡 Highlights

* End-to-end ML system (Data → Model → API → UI)
* Clean, modular architecture
* Real-time prediction via REST API
* Interactive and user-friendly frontend

---

## 📜 License

This project is intended for educational purposes and can be extended for production use.

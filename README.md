# E-commerce Revenue Forecast Dashboard

This project predicts and visualizes daily e-commerce revenue using **Python, Prophet, and Plotly Dash**.

## Overview
The project includes data cleaning, feature engineering, time series forecasting with Facebook Prophet, and an interactive dashboard for visualization.

## Features
- Daily revenue calculation and data preprocessing using Pandas  
- Prophet model for future revenue forecasting  
- Model evaluation using MAE and RMSE metrics  
- Interactive visualization built with Plotly Dash (zoom, pan, autoscale, etc.)

## Tech Stack
- Python 3.12  
- Pandas, NumPy, Scikit-learn  
- Plotly Dash, Prophet  

## Project Structure
```
e-commerce_forecast/
│
├── app.py # Dash dashboard
├── forecast_model.ipynb # Prophet model and analysis
├── data/ # Dataset folder
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

## How to Run
1. Clone the repository  
2. Install dependencies:
    ```bash
   pip install -r requirements.txt```
3. python app.py
4. Open in your browser: http://127.0.0.1:8050/

Author
Developed by Cihan
Informatik Student at THWS – focusing on Machine Learning, AI, and Data Analysis.
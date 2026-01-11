# E-Commerce Revenue Forecast Dashboard

An end-to-end time series forecasting project that analyzes historical e-commerce transactions
and predicts future daily revenue using Facebook Prophet, with results visualized in an
interactive Plotly Dash dashboard.

## Overview

The goal of this project is to understand revenue trends in an e-commerce dataset and forecast
future sales. The workflow covers the full data science pipeline: data cleaning, feature
engineering, time series modeling with Prophet, model evaluation, and deployment of results
in an interactive web dashboard.


## Features

- Cleaned and preprocessed raw transactional data (handling cancellations, missing values)
- Aggregated daily revenue from invoice-level data using Pandas
- Built and trained a Prophet time series model to forecast future revenue
- Evaluated model performance using MAE and RMSE
- Developed a simple interactive dashboard with Plotly Dash for visualizing actual vs predicted revenue


## Tech Stack
- Python 3.10+  
- Pandas, NumPy, Scikit-learn  
- Plotly Dash, Prophet  
- Docker (optional)

## Project Structure
```
e-commerce_forecast/
│
├── app.py
├── e_commerce_project.ipynb
├── data/
│   ├── data.csv
│   └── comparison.csv
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md

```

## Version Control

The repository includes a `.gitignore` file to exclude virtual environments,
temporary files, and Jupyter Notebook checkpoints from version control.

## How to Run
1. Clone the repository  
    ```bash
   git clone https://github.com/CihanC1/e-commerce_forecast.git
   cd e-commerce_forecast
    ```
2. Create and activate a virtual environment:
    Windows(Powershell/CMD)
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
   ```
    macOS / Linux:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
   ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
   ```
4. Run the application:
    ```bash
    python app.py
   ```
5. Open in your browser: 
    ```md
    http://127.0.0.1:8050/
    ```

## Optional: Run with Docker

The project can also be run inside a Docker container.
1. Build the Docker image:
    ```bash
    cd e-commerce_forecast
    docker build -t e-commerce-forecast .
   ```
2. Run the Docker container:
    ```bash
    docker run -p 8050:8050 e-commerce-forecast
    ```
3. Open in your browser:
    ```md
    http://127.0.0.1:8050/
    ```


## Author
**Cihan Can**  
B.Sc. Informatik Student at THWS  
Focus: Machine Learning, AI, Data Analysis
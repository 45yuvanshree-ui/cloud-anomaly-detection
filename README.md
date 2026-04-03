# Cloud Log Anomaly Detection System

## Overview

This project is a Machine Learning-based Intrusion Detection System (IDS) designed to detect anomalies in AWS cloud logs. It analyzes large-scale cloud activity data and identifies unusual patterns that may indicate security threats.

## Objectives

* Detect anomalies in AWS cloud logs
* Improve cloud security monitoring
* Provide insights through a web application
* Deploy the system in a cloud environment

## Technologies Used

* Python
* Flask
* Scikit-learn (Isolation Forest)
* Pandas, NumPy
* Matplotlib
* Render (Cloud Deployment)

## System Architecture

The system works in the following steps:

1. Load AWS log dataset
2. Perform feature engineering using frequency mapping
3. Scale the data
4. Apply Isolation Forest for anomaly detection
5. Display results through a Flask web application

## Features

* Detects anomalous cloud activities
* Displays total records and anomaly count
* Provides visualization of anomaly distribution
* Handles large datasets efficiently

## Sample Output

Total Records: around 1.9 million
Anomalies Detected: around 43,000

## How to Run Locally

Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open in browser:
http://127.0.0.1:5000

## Deployment

The project is deployed using Render cloud platform.

## Project Structure

```
app.py
model.pkl
scaler.pkl
tfidf.pkl
ip_map.pkl
event_map.pkl
region_map.pkl
requirements.txt
Procfile
```


## Challenges and Solutions

The project faced challenges such as handling large datasets, high anomaly detection rates, and deployment issues. These were handled using efficient preprocessing, improved feature engineering, and lightweight deployment using Flask and Render.

## Future Improvements

* Real-time anomaly detection
* Dashboard with interactive charts
* Integration with AWS services

## Author

Yuvan Shree

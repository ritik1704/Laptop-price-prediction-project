# Laptop Price Prediction Project
## Overview
This project focuses on analyzing and predicting laptop prices using a comprehensive dataset. The analysis includes Exploratory Data Analysis (EDA) to extract patterns and insights, feature extraction, and data processing. Key attributes like company, type, screen resolution, touch screen functionality, etc., were visualized to understand their influence on price. Correlation analysis helped in selecting the most relevant features.

Various machine learning models were trained, including **Linear Regression**, **Ridge Regression**, **Lasso**, **KNN**, **Random Forest**, **Decision Tree**, **AdaBoost**, and **SVM**, to evaluate their predictive performance. Metrics like **R²** and **Mean Absolute Error (MAE)** were used for comparison. The best-performing model was saved for deployment as a web application using Flask.

The project was deployed on **Render** to make the model accessible to users.

You can access the deployed project here:  
[Laptop Price Prediction Web App](https://laptop-price-prediction-project.onrender.com/)

## Project Structure

### 1. Exploratory Data Analysis (EDA)
- Conducted visualizations to explore the relationships between features like:
  - Laptop brand (company) and price.
  - Type of laptop (e.g., Notebook, Ultrabook) and price.
  - Screen resolution and its correlation with pricing.
  - Influence of touch screen availability on price.
- Extracted new features to enhance prediction accuracy.

### 2. Data Cleaning and Preprocessing
- Handled missing values and outliers to ensure data quality.
- Encoded categorical variables and extracted numerical sections from few categorical columns.
- Created a subset of features based on their correlation with the target variable, **Price**.

### 3. Model Building and Evaluation
- Trained multiple machine learning models for price prediction.
- Evaluated models using metrics:
  - **R² Score** for goodness of fit.
  - **Mean Absolute Error (MAE)** for prediction accuracy.
- Identified the best-performing model and saved it using the `pickle` library for deployment.

### 4. Deployment Stage
- Built a web application using the **Flask** framework.
- Deployed the application on **Render**, allowing users to input laptop features and receive price predictions.
## Data Source
The dataset used in this project provides comprehensive information about various laptops, including specifications and prices. It is ideal for analyzing the factors that influence laptop pricing and building predictive models. The Dataset used in the project is attached to this repository.



## Dependencies Installation
To run the project locally, install the necessary dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

For deployment-specific requirements, refer to the apprequirements.txt file and install them similarly:

```bash
pip install -r apprequirements.txt
```
## Running Project Locally

## Steps to Execute

### 1. EDA and Feature Engineering
- Open the `laptop-price-predictor.ipynb` file using Jupyter Notebook or Anaconda.
- Run all cells sequentially to:
  - Perform Exploratory Data Analysis (EDA).
  - Preprocess the dataset and engineer features.

### 2. Model Building and Evaluation
- Follow the steps in the notebook to:
  - Train machine learning models.
  - Evaluate the performance of each model.
- Save the best-performing model and the dataframe for deployment.

### 3. Web Application Deployment
- Run the `flaskapp.py` file to start the Flask web application locally.




## Contact

For any questions or feedback, please contact Ritik Suri at [Ritik1704@gmail.com](mailto:Ritik1704@gmail.com).
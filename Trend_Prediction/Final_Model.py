# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:31:42 2023

@author: Nathan
"""
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load the COVID-19 case data in CSV format
data = pd.read_csv('COVID-19_case_counts_by_date.csv')

# Convert the 'Date' column to a datetime object with format '%m/%d/%Y'
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Define the start and end dates for the analysis
start_date = '2021-07-01'
end_date = '2021-12-30'

# Convert the start and end dates to timestamps
start_timestamp = pd.Timestamp(start_date)
end_timestamp = pd.Timestamp(end_date)

# Filter the data for the specified date range (six months)
data_6_months = data.loc[(data['Date'] >= start_timestamp) & (data['Date'] <= end_timestamp)]

# Check if there are any data points for the next 3 months
data_next_3_months = data_6_months.loc[(data_6_months['Date'] > '2021-09-30') & (data_6_months['Date'] <= '2021-12-30')]
if len(data_next_3_months) == 0:
    print("No data points for the next 3 months.")
else:
    # Split the data into two parts: the first 3 months and the next 3 months
    data_first_3_months = data_6_months.loc[data_6_months['Date'] <= '2021-09-30']
    data_next_3_months = data_6_months.loc[(data_6_months['Date'] > '2021-09-30') & (data_6_months['Date'] <= '2021-12-30')]

    # Fit a polynomial regression model to the data from the first 3 months
    X = pd.to_numeric(pd.to_datetime(data_first_3_months['Date']))
    X = X.values.reshape(-1, 1)
    y = data_first_3_months['Total_cases'].values.reshape(-1, 1)
    polynomial_features = PolynomialFeatures(degree=11)
    X_poly = polynomial_features.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)

    # Make predictions for the next 3 months using the fitted model
    X_pred = pd.to_numeric(pd.to_datetime(data_next_3_months['Date']))
    X_pred = X_pred.values.reshape(-1, 1)
    X_pred_poly = polynomial_features.transform(X_pred)
    y_pred = model.predict(X_pred_poly)

    # Plot the predicted and actual data
    plt.plot(data_first_3_months['Date'], data_first_3_months['Total_cases'], label='Actual (First 3 Months)')
    plt.plot(data_next_3_months['Date'], y_pred, label='Predicted (Next 3 Months)')
    plt.plot(data_6_months['Date'], data_6_months['Total_cases'], label='Actual (Full 6 Months)')
    plt.title('COVID-19 Cases in 2021: Actual vs Predicted')
    plt.xlabel('Month')
    plt.ylabel('Total Cases')
    plt.legend()
    plt.show()



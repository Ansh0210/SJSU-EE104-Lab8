# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 02:42:07 2023

@author: Nathan
"""
# Import necessary libraries
import pandas as pd

# Load the loan data from a CSV file
loan_data = pd.read_csv('hmeq.csv')

# Define the risk factor thresholds for categorizing loans
low_risk_threshold = 0.2
medium_low_risk_threshold = 0.4
medium_high_risk_threshold = 0.6
high_risk_threshold = 0.8

# Calculate the risk factor for each loan
# Calculate the risk factor as the ratio of derogatory marks (DEROG) and delinquencies (DELINQ) to the credit length (CLAGE) normalized by 12 months 
loan_data['risk_factor'] = (loan_data['DEROG'] + loan_data['DELINQ']) / (loan_data['CLAGE'] / 12)

# Categorize each loan based on its risk factor and other features
# Define a function to assign risk categories based on loan and borrower characteristics
def assign_risk_category(row):
    # High-risk criteria: bad status (BAD) or certain occupations ('Self', 'Sales')
    if row['BAD'] == 1 or row['JOB'] in ('Self', 'Sales'):
        return 'high risk'
    # Low-risk criteria: debt consolidation loan, specific loan and mortgage due amount thresholds,
    #                   property value threshold, minimum job tenure (YOJ), no derogatory marks or delinquencies,
    #                   maximum credit inquiries (NINQ), maximum credit lines (CLNO), and maximum debt-to-income ratio (DEBTINC)

    elif row['REASON'] == 'DebtCon' and row['LOAN'] <= 20000 and row['MORTDUE'] <= 150000 and row['VALUE'] >= 75000 and row['YOJ'] >= 2 and row['DEROG'] == 0 and row['DELINQ'] == 0 and row['NINQ'] <= 1 and row['CLNO'] <= 12 and row['DEBTINC'] <= 30:
        return 'low risk'
    # Low-risk criteria: home improvement loan, specific loan and mortgage due amount thresholds,
    #                   property value threshold, minimum job tenure (YOJ), no derogatory marks or delinquencies,
    #                   maximum credit inquiries (NINQ), maximum credit lines (CLNO), and maximum debt-to-income ratio (DEBTINC)
    elif row['REASON'] == 'HomeImp' and row['LOAN'] <= 15000 and row['MORTDUE'] <= 100000 and row['VALUE'] >= 50000 and row['YOJ'] >= 2 and row['DEROG'] == 0 and row['DELINQ'] == 0 and row['NINQ'] <= 1 and row['CLNO'] <= 8 and row['DEBTINC'] <= 30:
        return 'low risk'
    # Default to medium risk if none of the specific criteria are met
    else:
        return 'medium risk'
    
# Categorize each loan's status based on its risk category
# Define a function to assign recommendation categories based on risk categories and specific loan criteria
def assign_recommendation_category(row):
    # Rejected: bad status (BAD) or certain occupations ('Self', 'Sales')
    if row['BAD'] == 1 or row['JOB'] in ('Self', 'Sales'):
        return 'REJECTED'
    # Approved: debt consolidation loan, specific loan and mortgage due amount thresholds,
    #           property value threshold, minimum job tenure (YOJ), no derogatory marks or delinquencies,
    #           maximum credit inquiries (NINQ), maximum credit lines (CLNO), and maximum debt-to-income ratio (DEBTINC)
    elif row['REASON'] == 'DebtCon' and row['LOAN'] <= 20000 and row['MORTDUE'] <= 150000 and row['VALUE'] >= 75000 and row['YOJ'] >= 2 and row['DEROG'] == 0 and row['DELINQ'] == 0 and row['NINQ'] <= 1 and row['CLNO'] <= 12 and row['DEBTINC'] <= 30:
         return 'APPROVED'
     # Approved: home improvement loan, specific loan and mortgage due amount thresholds,
    #           property value threshold, minimum job tenure (YOJ), no derogatory marks or delinquencies,
    #           maximum credit inquiries (NINQ), maximum credit lines (CLNO),
    elif row['REASON'] == 'HomeImp' and row['LOAN'] <= 15000 and row['MORTDUE'] <= 100000 and row['VALUE'] >= 50000 and row['YOJ'] >= 2 and row['DEROG'] == 0 and row['DELINQ'] == 0 and row['NINQ'] <= 1 and row['CLNO'] <= 8 and row['DEBTINC'] <= 30:
         return 'APPROVED'
    else:
         return 'CONDITIONAL APPROVED'
     
loan_data['risk_category'] = loan_data.apply(assign_risk_category, axis=1)
loan_data['assign_recommendation_category'] = loan_data.apply(assign_recommendation_category, axis=1)

# Save the loan data with risk categories and recommendation to a new CSV file
loan_data.to_csv('loan_data_with_risk_categories.csv', index=False)

# Output the loan data with risk categories
print(loan_data)


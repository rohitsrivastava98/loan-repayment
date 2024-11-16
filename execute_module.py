#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Utility to generate EMI Amount and repayment schedule for the provided loan details

Created on Sat Nov 16 21:24:09 2024

@author: rohit

Args:
    None
    
Usage:
   python execute_module 
"""

if __name__ == "__main__":
    print('Welcome in Loan EMI and Repayment Schedule Generator')
    loan_principal_amount = input('Please Provide Loan Amount')
    loan_roi = input('Please provide rate of interest')
    loan_tenure = input('Please provide loan tenure in months')
    loan_emi_date = input('Please provide emi date (1-22)')
    print(f'Loan Amount: {loan_principal_amount}\nLoan ROI: {loan_roi}\nLoan Tenure: {loan_tenure} Months\nEMI Date: {loan_emi_date}')
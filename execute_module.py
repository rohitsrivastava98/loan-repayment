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


from com.loan.repayment.dto.loan_application_dto import LoanApplicationDTO
from com.loan.validator.input_validator import InputValidator


if __name__ == "__main__":
    print('Welcome in Loan EMI and Repayment Schedule Generator')
    loan_principal_amount = input('Please Provide Loan Amount')
    loan_roi = input('Please provide rate of interest')
    loan_tenure = input('Please provide loan tenure in months')
    loan_emi_date = input('Please provide emi date (1-22)')
    loan_application_data = LoanApplicationDTO(loan_principal_amount, loan_tenure, loan_roi, loan_emi_date)
    input_validator = InputValidator()
    if input_validator.validateInput(loan_application_data):
        print('Input is correct')
    else:
        print('Data validation error')
        
    
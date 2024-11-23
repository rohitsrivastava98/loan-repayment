#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:05:14 2024

@author: rohit
"""

class LoanApplicationDTO:
    
    def __init__(self, loan_amount, loan_tenure, loan_roi, loan_emi_date):
        self.loan_amount = loan_amount
        self.loan_tenure = loan_tenure
        self.loan_roi = loan_roi
        self.loan_emi_date = loan_emi_date
        
        
    def get_data_values(self):
        
        return self.loan_amount, self.loan_tenure, self.loan_roi, self.loan_emi_date
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:39:19 2024

@author: rohit
"""

from datetime import date
from dateutil.relativedelta import relativedelta
from com.loan.repayment.dto.loan_emi_dto import LoanEmiDTO

class EmiDataGenerator:
    
    def __init__(self):
        print('Creating object for class EmiDataGenerator')
        
        
    def get_principal_component(interest_component,  loan_emi):
        
        return loan_emi - interest_component
    
    
    def get_interest_component(loan_principal, loan_emi, loan_tenure):
        
        return float(14000)
    
    
    def get_emi_date(first_emi_date: date, emi_number):
        
        if emi_number == 1:
            return first_emi_date
        else:
            return first_emi_date + relativedelta(months=+emi_number)
        
        
    def calculate_month_emi(self, loan_principal, emi_number, loan_roi, first_emi_date) -> LoanEmiDTO:
        emi_date = self.get_loan_emi_dataemi_date(first_emi_date, emi_number)
        interest_component = self.get_interest_component(loan_emi, loan_tenure)
        
        
        
    
    
    
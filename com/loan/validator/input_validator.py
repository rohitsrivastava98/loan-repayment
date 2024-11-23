#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 15:57:32 2024

@author: rohit
"""


from com.loan.repayment.dto.loan_application_dto import LoanApplicationDTO

class InputValidator:
    
    def validateInput(self, loan_application_dto: LoanApplicationDTO):
        
           loan_amount, loan_tenure, loan_roi, loan_emi_date = loan_application_dto.get_data_values()
           
           try:
               loan_amount = float(loan_amount)
               loan_tenure = int(loan_tenure)
               loan_roi = float(loan_roi)
               loan_emi_date = int(loan_emi_date)
               loan_application_dto = LoanApplicationDTO(loan_amount, loan_tenure, loan_roi, loan_emi_date)
               return True
           except ValueError as e:
                print("Invalid Input data type", e)
                return False
                
           except Exception as e:
                print("Unexpected error occurred. Please try after some time", e)
                return False
                   
    
    
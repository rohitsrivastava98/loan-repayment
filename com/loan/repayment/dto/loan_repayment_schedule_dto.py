#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:40:56 2024

@author: rohit
"""


from loan_emi_dto import LoanEmiDTO


class LoanRepaymentScheduleDTO:
    
      
    def __init__(self, emi_amount):
        self.emi_amount = emi_amount
        self.emi_list = []
        
        
    def add_emi_data(self, loan_emi_data):
        if isinstance(loan_emi_data, LoanEmiDTO):
            self.emi_list.append(loan_emi_data)
        else:
            raise ValueError('Passed value must be of type LoanEmiDTO')
            
            
    def get_values(self):
        return self.emi_amount, self.emi_list
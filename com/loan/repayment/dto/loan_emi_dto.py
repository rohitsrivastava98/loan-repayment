#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:46:50 2024

@author: rohit
"""


from datatime import date


class LoanEmiDTO:
    
    def __init__(self, emi_date: date, principal_amount: float, interest_amount: float):
        self.emi_date = emi_date
        self.principal_amount = principal_amount
        self.interest_amount = interest_amount
        
        
    def get_emi_data(self):
        return self.emi_date, self.principal_amount, self.interest_amount
        
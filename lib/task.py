#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:05:35 2018

@author: ygor
"""

class taskModel:
  
    def __init__(self):
        self.status = 0
        
    def execute(self):
        self.status = 1

    def complete(self): 
        self.status = 2
    
        
        
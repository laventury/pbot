#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""

from lib import schedule
from datetime import datetime

class taskModel:    
        
    def scheduleJob(self):
        scheduleJob = schedule.every().minute.tag('t0002','tasks')
        return scheduleJob
        
    def job(self):
        print("rodando task 2 : ",datetime.now())                         
        


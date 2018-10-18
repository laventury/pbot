#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:57:46 2018

@author: Ygor Pitombeira
"""

from lib.task import taskModel
from datetime import datetime

class taskChild(taskModel):

    def __init__(self, id):
        super().__init__(id)
        self.scheduleJob.interval = 2
        self.scheduleJob.unit = 'minutes'
        self.scheduleJob.start(datetime(2018,10,18,13,39))

    def job(self):
        print(str(self.scheduleJob.interval) + " " + self.scheduleJob.unit)
        print("rodando task 1 : ",datetime.now())
        


task = taskChild('t0001')
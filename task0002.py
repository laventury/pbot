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
        self.scheduleJob.interval = 10
        self.scheduleJob.unit = 'seconds'

    def job(self):
        print("rodando task 2 : ",datetime.now())


task = taskChild('t0002')
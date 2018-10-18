#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:57:46 2018

@author: Ygor Pitombeira
"""

from lib.task import taskModel
from datetime import datetime

class taskChild(taskModel):

    def set_schedule(self):
        return self.scheduleJob.second

    def job(self):
        print("rodando task 1 : ",datetime.now())


task = taskChild('t0001')
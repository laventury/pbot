#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
import traceback

class taskModel:

    def __init__(self, id, value_interval):
        self.id = id
        self.scheduleJob = schedule.every(value_interval).tag(id)

    def set_schedule(self):
        pass

    def job(self):
        pass

    def execJob(self):
        try:
            self.job()
        except:
            print(traceback.format_exc())
            schedule.cancel_job(self.scheduleJob)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
from datetime import datetime
import traceback
import configparser
import os

class taskModel:

    def __init__(self, id):

        self.id = id
        
        path = os.path.join(os.getcwd(),"data")
        self.configFile = os.path.join(path, id + ".cfg")

        config = configparser.ConfigParser()
        
        if os.path.isfile(self.configFile):     
            config.read(self.configFile)
            config_last_run = datetime.strptime(config['Job']['last_run'],'%d/%m/%Y %H:%M')
            
        else:
            config_last_run = ''
            config['Job'] = {}
            config['Job']['last_run'] = ''
            with open(self.configFile, 'w') as configfile:
                config.write(configfile)
       
        self.config = config

        self.scheduleJob = schedule.every().tag(id)

        if config_last_run:
           self.scheduleJob.last_run = config_last_run 
        

    def job(self):
        pass

    def execJob(self):
        try:
       
            self.job()
    
            strLast_run = self.scheduleJob.last_run.strftime('%d/%m/%Y %H:%M')
            self.config['Job']['last_run'] = strLast_run
            with open(self.configFile, 'w') as configfile:
                self.config.write(configfile)
 
        except:
            print(traceback.format_exc())
            schedule.cancel_job(self.scheduleJob)




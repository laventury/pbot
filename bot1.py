# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
import time
import glob

  
def main():

    taskfiles = [x[:-3] for x in glob.glob("*.py") if x.find("task") != -1]
    taskfiles.sort()
    
    for tasklib in taskfiles:
        
        task = __import__(tasklib)
        Currentask = task.taskModel()  
        setSchedule = Currentask.setSchedule() 
        setSchedule.do(Currentask.job) 
  
    while 1:
        schedule.run_pending()
        time.sleep(1)    
   
           
if __name__ == "__main__":
    main()







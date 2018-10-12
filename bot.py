# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira    
"""
from lib import schedule
import time
<<<<<<< HEAD
import threading
import glob

jobqueue = queue.Queue()
botJobs = set()

def worker_main():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()


def loadTasks():
    global botJobs
    taskfiles = [x[:-3] for x in glob.glob("*.py") if x.find("task") != -1]
    taskfiles.sort()
    
    for tasklib in taskfiles:       
        task = __import__(tasklib)
        Currentask = task.taskModel()  
        scheduleJob = Currentask.scheduleJob()
        if not botJobs >= scheduleJob.tags:
            scheduleJob.do(jobqueue.put, Currentask.job)
            botJobs |= scheduleJob.tags

  
def main():
    schedule.every(30).seconds.do(loadTasks).run()

    worker_thread = threading.Thread(target=worker_main)
    worker_thread.start()
=======

from task0001 import t0001
  
def main():

    schedule.every(10).seconds.do(t0001.execute)
>>>>>>> parent of 1a2c80d... shedule task periodic complete

    while True:
        schedule.run_pending()
        time.sleep(1)
           
if __name__ == "__main__":

    main()


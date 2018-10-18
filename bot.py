# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
import time
import threading
import queue
import glob

jobqueue = queue.Queue()
botJobs = set()

def worker_main():
    while True:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()

def loadTasks():
    global botJobs
    taskfiles = [x[:-3] for x in glob.glob("*.py") if x.find("task") != -1]
    taskfiles.sort()

    for taskfile in taskfiles:
        tasklib = __import__(taskfile)
        Currentask = tasklib.task
        if not botJobs >= Currentask.scheduleJob.tags:
            Currentask.scheduleJob.do(jobqueue.put, Currentask.execJob)
            botJobs |= Currentask.scheduleJob.tags

def main():

    schedule.every(1).day.do(loadTasks).run()

    worker_thread = threading.Thread(target=worker_main)
    worker_thread.start()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":

    main()


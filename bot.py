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

# jobqueue - Pilha de execucao de trabalhos
# botJobs - Set de trabalho do Bot (Controle trabalhos sendo executados)
jobqueue = queue.Queue()
botJobs = set()

# Rotina de execucao principal
# puxa o trabalho do topo da pilha e executa
def worker_main():
    while True:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()


# Rotina de Carregamento de trabalhos na pilha
# verifica se existe novo arquivo de rotina de trabalho
# carrega na pilha de trabalhos e atualiza o set de trabalhos 
# para evitar inclusão de trabalhos em duplicidade na pilha
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
    # Coloca na agenda a rotina 1 - Carregamento e trabalhos
    schedule.every(1).day.do(loadTasks).run()

    # Carrega rotina principal na mermoria de exec 
    worker_thread = threading.Thread(target=worker_main)
    worker_thread.start()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":

    main()


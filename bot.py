# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""

import glob

  
def main():
 
    taskfiles = [x[:-3] for x in glob.glob("*.py") if x.find("task") != -1]
    taskfiles.sort()
    
    for tasklib in taskfiles:
        try:            
            task = __import__(tasklib).task_X          
        except ImportError:
            print("Erro na importação da tarefa %s"%(tasklib))
          
        task.execute()
            
if __name__ == "__main__":
    main()


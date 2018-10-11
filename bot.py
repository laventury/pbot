# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
import time

from task0001 import t0001
  
def main():

    schedule.every(10).seconds.do(t0001.execute)

    while True:
        schedule.run_pending()
        time.sleep(1)
           
if __name__ == "__main__":
    main()


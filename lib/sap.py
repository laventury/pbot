# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:25:20 2018

@author: wu3y
"""

import os
import re
import subprocess
import time

class sapvbs:

    def __init__(self, SapFile, OutputFile):
    
        self.path = os.path.join(os.getcwd(),"data")
        self.sapFile = SapFile
        self.sapFilePath = os.path.join(self.path,self.sapFile)
        self.outputFile = OutputFile  
        self.outputFilePath = os.path.join(self.path,self.outputFile)
        self.vbsTemplate = open(self.sapFilePath,"r").read()
        # Ajuste do VBscript
        self.vbs = re.sub("(#PATH#)",self.path,self.vbsTemplate)
        self.vbs = re.sub("(#FILEOUTPUT#)",self.outputFile ,self.vbs)

    def subs(self, subs):
        for sub in subs:
            self.vbs = re.sub("(%s)"%(sub[0]),sub[1] ,self.vbs)

    def execute(self):     

        if os.path.isfile(self.outputFilePath):
            os.remove(self.outputFilePath)

        tempVbsFile = os.path.join(self.path,"temp.vbs")
        
        open(tempVbsFile,"w+").write(self.vbs)        
        
        subprocess.check_call(tempVbsFile, shell=True)
        
        os.remove(tempVbsFile)
        
 
    def openSAP(self, connectFile): 
        connectFilePath = os.path.join(self.path, connectFile)
        ret = subprocess.check_call(connectFilePath, shell=True)
        time.sleep(5)
        return not ret
        
        
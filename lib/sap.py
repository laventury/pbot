# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:25:20 2018

@author: wu3y
"""

import os
import re
import subprocess

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

        if os.path.isfile(self.outputFile):
            os.remove(self.outputFile)
                    
        subprocess.check_call(self.SapFile, shell=True)
    
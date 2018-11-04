# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:42:51 2018

@author: ygor Pitombeira

    Ler arquivo de dados em formato de texto,
    aplica regex a partir de um arquivo pattern 
    
    Entrada : Arquivo de texto
    Saida : [('AAA','bbb'),('ddd','www')]
"""

import re
import os

class regex:
     
    def __init__(self, Data, Path=None, PathSec=None, Regex=None, File=None):

        if Path:
            self.Path = Path
        else:
            self.Path = os.getcwd()
            
        if PathSec:
            self.PathSec = PathSec
        else:
            self.PathSec = os.path.join(self.Path, 'data')
        
        self.Regex = Regex
        
        self.File = File
        if File:
            self.File = os.path.join(self.PathSec,File)
  
        self.Data = Data
        if Data:
            self.Data = os.path.join(self.PathSec,Data)
            
        self.pattern = None
        pattern = None
        if self.Regex:
            pattern = self.Regex
        else:
            if self.File:
                pattern = open(self.File,"r").read()
        
        if pattern:
            self.pattern = re.compile(pattern)
        
        columnsrow = list(self.pattern.groupindex.keys())
        columns = []
        
        for col in columnsrow:
            colnt = col.split('__')
            columns.append((colnt[0],colnt[1].upper()))
            
        self.columns = columns
        self.result = None
        
    def execute(self):
        DataFile = open(self.Data,"r").read()
        #Convertendo datas de padrão SAP para padrao SQL
        DataFile = re.sub('(\d{2}).(\d{2}).(\d{4})','\g<3>-\g<2>-\g<1>',DataFile)
        #Aplicando regex no arquivo de dados
        if self.pattern:        
            self.result = self.pattern.findall(DataFile)
        return self
